from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.gateway.pokt.network/v1/lb/635700cdd6e6e4c4aacddaf7"))

print(w3.isConnected())