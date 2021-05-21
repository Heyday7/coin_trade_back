from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.PositiveBigIntegerField(default=100000000)


class Transaction(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='transactions',
        related_query_name='transaction'
    )
    type = models.CharField(max_length=10, default='buy')
    coin = models.ForeignKey('coin.Coin', on_delete=models.CASCADE)
    price = models.FloatField()
    total_price = models.FloatField()
    coin_amount = models.FloatField()

