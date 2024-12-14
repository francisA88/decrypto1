# payment_gateway/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Merchant, Payment
from .utils import create_wallet
from .service import check_transaction
# from .fiat_service import convert_crypto_to_fiat

class RegisterMerchant(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        fiat_currency = request.data.get("fiat_currency", "USD")
        
        wallet = create_wallet()
        merchant = Merchant.objects.create(
            name=name, email=email, public_key=wallet["public_key"],
            private_key=wallet["private_key"], fiat_currency=fiat_currency
        )
        return Response({"public_key": merchant.public_key}, status=201)

class ProcessPayment(APIView):
    def post(self, request):
        merchant_id = request.data.get("merchant_id")
        amount_crypto = request.data.get("amount_crypto")
        
        merchant = Merchant.objects.get(id=merchant_id)
        # Track payment in Solana (mock for now)
        payment = Payment.objects.create(merchant=merchant, amount_crypto=amount_crypto)
        return Response({"payment_id": payment.id}, status=201)
