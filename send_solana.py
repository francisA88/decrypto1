from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

# Destination wallet
destination = "DestinationPublicKeyHere"

# Create a transaction
txn = Transaction().add(
    transfer(
        TransferParams(
            from_pubkey=keypair.public_key,
            to_pubkey=destination,
            lamports=1000000  # 0.001 SOL
        )
    )
)

# Send the transaction
response = client.send_transaction(txn, keypair)
print("Transaction ID:", response["result"])
