from django.db import models

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=10)
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
    
