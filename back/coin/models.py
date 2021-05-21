from django.db import models

# Create your models here.


class Coin(models.Model):
    name = models.CharField(max_length=100, null=True)
    ticker = models.CharField(max_length=10)
    description = models.TextField(default=None, null=True)

    def __str__(self):
        return self.ticker


class CoinPrice(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    opening_price = models.FloatField()
    closing_price = models.FloatField()
    min_price = models.FloatField()
    max_price = models.FloatField()
    units_traded = models.FloatField()
    acc_trade_value = models.FloatField()
    prev_closing_price = models.FloatField()
    units_traded_24H = models.FloatField()
    acc_trade_value_24H = models.FloatField()
    fluctate_24H = models.FloatField()
    fluctate_rate_24H = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    

class CoinHolding(models.Model):
    account = models.ForeignKey(
        'account.Account', 
        on_delete=models.CASCADE,
        related_name='coinholdings',
        related_query_name='coinholding')
    price = models.FloatField()
    total_price = models.FloatField()
    coin_amount = models.FloatField()
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
