from __future__ import absolute_import, unicode_literals 
from celery import shared_task 
from .models import Coin, CoinPrice
import requests

# @shared_task
# def get_coin_data(ticker):
#     url = f'https://api.bithumb.com/public/ticker/{ticker}_KRW'
#     response = requests.get(url)
#     data = response.json()
#     coin, already = Coin.objects.get_or_create(ticker=ticker)
#     data['data']['coin'] = coin
#     if data['status'] == '0000':
#         CoinPrice.objects.create(**data['data'])
        