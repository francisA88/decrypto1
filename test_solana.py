from solders.keypair import Keypair
from solana.rpc.api import Client
from pybip39 import Mnemonic, Seed

DEVNET_URL = "https://api.devnet.solana.com"
# TESTNET_URL = "https://api.testnet.solana.com"

# client = Client(TESTNET_URL)

client = Client(DEVNET_URL)

# mnem = Mnemonic()

# mnemonic = mnem.from_phrase("season morning latin apology foil ancient balcony emotion bitter east verb cancel")
# help(Keypair)
seed_phrase = "season morning latin apology foil ancient balcony emotion bitter east verb cancel"#.encode('utf8')
passphrase = "beansonium"

keypair = Keypair.from_seed_phrase_and_passphrase(
    seed_phrase=seed_phrase,
    passphrase=passphrase
)

ADDRESS_PK = keypair.pubkey()
balance = client.get_balance(ADDRESS_PK)#['result']

# print(dir(balance))
print('balance: ', balance.value)

print(keypair)
print(type(keypair))
print(dir(Keypair))