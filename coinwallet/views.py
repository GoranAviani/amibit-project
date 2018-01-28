from django.shortcuts import render,redirect,get_object_or_404
from coinwallet.models import CoinWallet

from coinwallet.forms import (
CoinWalletCreateForm,
)


# Create your views here.
def CoinWalletDashboardView(request):
    if request.user.is_authenticated():

            queryWallet = CoinWallet.objects.filter(wallet_user=request.user)
            return render(request, 'coinwallet/coinwallet_dashboard.html', {
            'queryWallet': queryWallet,
            })
    else:
        return render(
        request,
        'coinwallet/coinwallet_dashboard.html'
    )


def CoinWalletCreateView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_coinwallet_create = CoinWalletCreateForm(request.POST)
            if form_coinwallet_create.is_valid():
                form = form_coinwallet_create.save(commit=False)
                form.wallet_user = request.user
                form.save()
            return redirect('coinwallet_dashboard')
        else:
            form_coinwallet_create = CoinWalletCreateForm()
            return render(request, 'coinwallet/coinwallet_create.html', {'form_coinwallet_create': form_coinwallet_create})
    else:
        return render(request,'perasis/not_authenticaded.html')


def CoinWalletUpdateView(request,id):
    coin_to_update = get_object_or_404(CoinWallet, id=id)
    if request.user.is_authenticated():
        if coin_to_update.wallet_user == request.user:
            if request.method == 'POST':
                form_coinwallet_update = CoinWalletCreateForm(request.POST)
                if form_coinwallet_update.is_valid():
                    form = form_coinwallet_update.save(commit=False)
                    form.id = id
                    form.wallet_user = request.user
                    form.save()
                    return redirect('coinwallet_dashboard')
            else:
                form_coinwallet_update = CoinWalletCreateForm(instance = coin_to_update)
                return render(request, 'coinwallet/coinwallet_update.html', {'form_coinwallet_update': form_coinwallet_update})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        return render(request,'perasis/not_authenticaded.html')

def CoinWalletDeleteView(request,id):
    coin_to_delete = get_object_or_404(CoinWallet, id=id)
    if request.user.is_authenticated():
        if coin_to_delete.wallet_user == request.user:
            if request.method == 'POST':
                form_coinwallet_delete = CoinWalletCreateForm(request.POST)
                if form_coinwallet_delete.is_valid():
                    coin_to_delete.delete()
                    return redirect('coinwallet_dashboard')
            else:
                form_coinwallet_delete = CoinWalletCreateForm(instance=coin_to_delete)
                return render(request, 'coinwallet/coinwallet_delete.html', {'form_coinwallet_delete': form_coinwallet_delete})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        return render(request,'perasis/not_authenticaded.html')


import os
import json
import time
coin_wallet={'XLM':41.958,'MIOTA':26.973,'COSS':49,'APPC':11.98}
def read_prices_for_my_wallet(self):
    #code here

    os.system("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0 > prices.txt")

    wallet_sum=0
    with open('prices.txt', 'r') as content_file:
        content = content_file.read()
        sve = json.loads(content)
        #print(sve)
        print(coin_wallet)
        for x in coin_wallet:
        #    print([x])
        #    print(coin_wallet[x])
            for valuta in sve:
                if valuta['symbol'] == x:
                    print("currency: "+valuta['symbol']+ " cijena: " + valuta['price_usd'])
                    #vrijednost = ((valuta['price_usd']) )
                #    print( (coin_wallet[x]))
                    #print(vrijednost)
                    vrijednost = (float(valuta['price_usd']) * float(coin_wallet[x]))
                    wallet_sum += vrijednost
                    #print("Imas: "+str([x])+ " i to je: " + str(vrijednost))
                    print(vrijednost)
        print("sve skupa: "+ "%.2f" % round(wallet_sum,2) )

    time.sleep(60)

#while True:
#    read_prices_for_my_wallet(coin_wallet)
