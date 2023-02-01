from neo4j import GraphDatabase
from etherscan import Transactions

class TxWriter:
    def __init__(self, session, api_key, address):
        self.session = session  # neo4j driver session
        self.api_key = api_key
        self.address = address
    def relation(self):
        account = Transactions(self.api_key, self.address).normal_txns()
        relations = []
        for tx in account:
            relations.append((tx['from'], tx['to']))
        return relations
    
    def dbWriter(self, to_address, from_address):
        
        self.session.run(
            """MERGE (a:Account {address: $fromAddress})
            MERGE (b:Account {address: $toAddress})
            MERGE (a)-[:SENT]->(b)""",
            {"fromAddress": from_address, "toAddress": to_address}
        )
    
    def writer(self):
        for rel in self.relation():
            self.dbWriter(rel[0], rel[1])

