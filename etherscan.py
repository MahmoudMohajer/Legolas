# module for listing internal and external transactions
from requests import get
from datetime import datetime

class Transactions:
    def __init__(self, api_key, address) -> None:
        self.api_key = api_key
        self.address = address

    def make_api_url(self,module, action, address, **kwargs):
        BASE_URL = BASE_URL = 'https://api.etherscan.io/api'

        url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={self.api_key}"

        for key, value in kwargs.items():
            url += f'&{key}={value}'
    
        return url

    def internal_txns(self):
        url = self.make_api_url(module='account', action='txlistinternal', address=self.address, startblock=0, endblock=99999999, offset=10000, sort='asc')
        response = get(url)
        data = response.json()['result']
        return data

    def normal_txns(self):
        url = self.make_api_url(module='account', action='txlist', address=self.address, startblock=0, endblock=99999999, offset=10000, sort='asc')
        response = get(url)
        data = response.json()['result']
        return data
    
    def get_all_txns(self):
        data = self.normal_txns() + self.internal_txns()
        return data
        
        
if __name__ == '__main__':

    wallet_1 = Transactions(api_key='M69W5IYP6D8ENMNV5K1X2UKJS1BGX16SZG', address='0x228bB8BcbCEc34e5b2E82791D916E577FC6C6C7a' )

    for txn in wallet_1.get_all_txns():
        for key, value in txn.items():
            print(f'{key}: {value}')
        print(9*'-')