# payment_gateway/utils.py

from solders.keypair import Keypair

from pybip39 import Mnemonic

def create_temp_wallet():
    nem = Mnemonic()
    keypair = Keypair.from_seed_phrase_and_passphrase(
        seed_phrase=nem.phrase,
        passphrase=nem.phrase)

    s = ''
    for i in keypair.to_bytes_array():
        s += str(i) + '/'
    retrieval_string = s[:-1]

    return {
        "public_key": str(keypair.pubkey()),
        "private_key": keypair.secret_key.hex(),  # Store securely!
        "retrieval_string": retrieval_string
    }

def create_keypair_from_string(retrieval_string):
    bytes_array = retrieval_string.split('/')

    return Keypair().from_bytes(bytes(bytes_array))


