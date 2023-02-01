from requests import get

class ZkTrack:

    def __init__(self, address) -> None:
        self.address = address
    
    def create_api_url(self,module, address, action, tags):
        BASE_URL = "https://api.zksync.io/api/v0.2/"
        
        url = BASE_URL + f"{module}/{address}/{action}?"
        for key, value in tags.items():
            url += f"&{key}={value}"
        return url

    def get_transfers(self):
        url = self.create_api_url("accounts", self.address, "transactions", {'from':'latest', 'limit':70, 'direction':'older'})
        request = get(url)
        response = request.json()['result']['list']

        transactions = []
        for tx in response:
            
            if tx['op']['type'] == 'Transfer': 
                tx_doc = {}
                tx_doc['from'] = tx['op']['from']
                tx_doc['to'] = tx['op']['to']
                tx_doc['fee'] = int(tx['op']['fee']) / 10**18
                tx_doc['status'] = tx['status']
                tx_doc['createdAt'] = tx['createdAt']
                transactions.append(tx_doc)            

        return transactions
