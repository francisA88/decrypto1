import secrets

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Merchant, Payment
from .utils import create_temp_wallet

merchant_sk = ''
sk = ''

first_time_loading = True

def index(request):
    return render(request, 'index.html')

def flashcards(request):
    return render(request, 'flashcards.html')

def predashboard(request):
    # Quite similar to a login functionality
    global first_time_loading, merchant_sk

    first_time_loading = True

    if request.method.lower() == 'post':
        merchant_sk = request.POST['sk']
        return redirect('/dashboard')
    return render(request, 'pre.html')

# @login_required('/login')
def dashboard(request):
    try:
        global first_time_loading
        if not first_time_loading:
            print('here')
            return redirect('/pre')
        first_time_loading = False

        merchant = Merchant.objects.get(unique_sk=merchant_sk)
        transactions = Payment.objects.filter(merchant=merchant)

    except Merchant.DoesNotExist:
        return HttpResponse('Oops! Merchant does not exist in our world', status='400')
    
    context = {
        'merchant': merchant,
        'transactions': transactions
    }
    return render(request, 'dashboard.html', context)

def create_user(request):
    global sk, merchant_sk
    if request.method.lower() == 'post':
        sk = secrets.token_hex()
        merchant_sk = sk
        name = request.POST['name']
        email = request.POST['email']
        merc = Merchant(
            name=name,
            email=email,
            unique_sk=sk
        )
        sk = sk
        merc.save()
        # return HttpResponse(status=200) 
        return redirect('/view-key/')
    else:
        # return HttpResponse('Forbidden', status=403)
        return render(request, 'signup.html')
    
def create_payment(request, amount_in_sol):
    is_generated = False
    # if request.method.lower() == 'post':
    receiving_wallet = create_temp_wallet()
    pubkey = receiving_wallet['public_key']
    merchant = Merchant.objects.get(unique_sk=merchant_sk)
    is_generated = True

    return render(
        request, 
        'payment.html', 
        {
         'is_generated': is_generated,
         'amount_in_sol': amount_in_sol,
         'address': pubkey,
         'name': merchant.name,
         'details': 'dummy details'
         }
        )

def display_key(request):
    print(merchant_sk)
    return render(request, 'key_display.html', {
        'sk': merchant_sk[:10],
        'sk_full': merchant_sk})