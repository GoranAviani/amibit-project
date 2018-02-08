from django.shortcuts import render,redirect,get_object_or_404
from coinwallet.models import CoinWallet

import os
import json
import time


from coinwallet.forms import (
CoinWalletCreateForm,
)
# Create your views here.
class CryptoProtfolioValue():
    def __init__(self, prices_json,wallet_sum,wallet_sum_per_coin):
        self.prices_json=prices_json
        self.wallet_sum=wallet_sum
        self.wallet_sum_per_coin=wallet_sum_per_coin
    def get_prices(self,):
        prices = os.popen("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0").read()
        self.prices_json = json.loads(prices)
        #time.sleep(5)
    def print_my_portfolio_value(self,):
        wallet_sum_per_coin={}
        #queryCoinWallet_model=CoinWallet.objects.filter(wallet_user=request.user)
        queryCoinWallet_model = CoinWallet.objects.all() # ovde dohvaca sve , treba dohvacat samo od usera
        for x in queryCoinWallet_model:
            for valuta in self.prices_json:
                if valuta['symbol'] == x.wallet_coin:
                    worth_per_coin = (float(valuta['price_usd']) * float(x.wallet_amount))
                    self.wallet_sum += worth_per_coin
                    self.wallet_sum_per_coin.update({x.wallet_coin:worth_per_coin})
        self.wallet_sum = round(self.wallet_sum,2)

def CoinWalletDashboardView(request):
    if request.user.is_authenticated():
        Cryptotask = CryptoProtfolioValue("",0,{})
        #while True:
        Cryptotask.get_prices()
        Cryptotask.print_my_portfolio_value()
        queryWallet = CoinWallet.objects.filter(wallet_user=request.user)
        return render(request, 'coinwallet/coinwallet_dashboard.html', {
        'queryWallet': queryWallet,
        'wallet_sum':Cryptotask.wallet_sum,
        'wallet_sum_per_coin':Cryptotask.wallet_sum_per_coin,
        })
    else:
        return render(request,'perasis/not_authenticaded.html')


#old way:
#def CoinWalletDashboardView(request):
#    if request.user.is_authenticated():
#            prices = os.popen("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0").read()
#            wallet_sum=0
#            wallet_sum_per_coin={}
#            sve = json.loads(prices)
#            queryCoinWallet_model = CoinWallet.objects.all()
#            for x in queryCoinWallet_model:
#                for valuta in sve:
#                    if valuta['symbol'] == x.wallet_coin:
#                        #print("currency: "+valuta['symbol']+ " cijena: " + valuta['price_usd'])
#                        worth_per_coin = (float(valuta['price_usd']) * float(x.wallet_amount))
#                        wallet_sum += worth_per_coin
#                        wallet_sum_per_coin.update({x.wallet_coin:worth_per_coin})

                        #print("Imas: "+str([x])+ " i to je: " + str(vrijednost))
                    #    print(worth_per_coin)
#            wallet_sum = round(wallet_sum,2)

#            queryWallet = CoinWallet.objects.filter(wallet_user=request.user)
#            return render(request, 'coinwallet/coinwallet_dashboard.html', {
#            'queryWallet': queryWallet,
#            'wallet_sum':wallet_sum,
#            'wallet_sum_per_coin':wallet_sum_per_coin,
#            })
#    else:
#        return render(request,'perasis/not_authenticaded.html')








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
