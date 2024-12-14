# payment_gateway/models.py

from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    unique_sk = models.CharField(max_length=300, unique=True)
    # password = models.CharField(max_length=20)
    public_key = models.CharField(max_length=128)  # Solana wallet public key
    private_key = models.TextField()  # Encrypted private key (handle securely)
    fiat_currency = models.CharField(max_length=10, default="NAIRA")  # Preferred fiat currency
    fiat_account_number = models.CharField(max_length=10) # Receiving Nigerian bank account number. This is usually of 10 digits
    fiat_bank_name = models.CharField(max_length=50) # Receiving Nigerian bank name

class Payment(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="No description")
    amount_crypto = models.DecimalField(max_digits=18, decimal_places=8)  # Crypto amount
    amount_fiat = models.DecimalField(max_digits=12, decimal_places=2)  # Fiat equivalent
    status = models.CharField(max_length=20, default="PENDING")  # PENDING, COMPLETED, FAILED
    transaction_id = models.CharField(max_length=128, null=True, blank=True)  # Solana txn ID
    created_at = models.DateTimeField(auto_now_add=True)

    keypair_derivative = models.TextField() # Will be used to generate the bytes used to reconstruct the keypair 

class KeypairModel(models.Model):...
    
    
class ConversionRate(models.Model):
    crypto_symbol = models.CharField(max_length=10)  # e.g., SOL, USDC
    fiat_currency = models.CharField(max_length=10, default="USD")
    rate = models.FloatField()  # Conversion rate
    updated_at = models.DateTimeField(auto_now=True)
