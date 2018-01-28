from django.db import models

# Create your models here.
class CoinWallet(models.Model):
#CoinWallet model

    wallet_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    wallet_coin = models.CharField(max_length=50)
    wallet_amount = models.CharField(max_length=200)

    def __str__(self):
        return self.wallet_coin
