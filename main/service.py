# payment_gateway/solana_service.py

from solana.rpc.api import Client

SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC_URL)

def check_transaction(transaction_id):
    result = client.get_transaction(transaction_id)
    return result  # Parse this to confirm status

def check_balance(keypair):
    balance = client.get_balance(keypair.pubkey())
    return balance.value

def get_conversion_rate(amount_in_sol):
    ''' Returns an equivalent amount in naira or perhaps some other fiat currency. '''
    pass