from __future__ import absolute_import, unicode_literals 
from celery import shared_task 
from .serializers import CoinSerializer
from .models import Coin
import requests

@shared_task
def get_coin_data(coin):
    url = f'https://api.bithumb.com/public/ticker/{coin}_KRW'
    response = requests.get(url)
    data = response.json()
    data['data']['name'] = coin

    if data['status'] == '0000':
        Coin.objects.create(**data['data'])
        