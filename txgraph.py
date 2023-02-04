"""
this module is for creating nodes and relationships between two wallet addresses in the Neo4j graph database.
"""
from etherscan import Transactions

class TxWriter:
    def __init__(self, session, api_key, address):
        self.session = session
        self.api_key = api_key
        self.address = address
        self.relations = self.get_relations()
        
    def get_relations(self):
        account = Transactions(self.api_key, self.address).normal_txns()
        relations = [(tx['from'], tx['to']) for tx in account]
        return relations
        
    def write_to_db(self, to_address, from_address):
        query = """
        MERGE (a:Account {address: $fromAddress})
        MERGE (b:Account {address: $toAddress})
        MERGE (a)-[:SENT]->(b)
        """
        self.session.run(query, {"fromAddress": from_address, "toAddress": to_address})
    
    def write(self):
        for from_address, to_address in self.relations:
            self.write_to_db(to_address, from_address)
