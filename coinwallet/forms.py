from django import forms
from coinwallet.models import CoinWallet
from django.contrib.auth.models import User


class CoinWalletCreateForm(forms.ModelForm):
    wallet_coin = forms.CharField()
    wallet_amount = forms.CharField()
    class Meta:
        model = CoinWallet
        fields = (
            'wallet_coin',
            'wallet_amount',
            )
