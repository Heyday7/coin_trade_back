from __future__ import absolute_import, unicode_literals 
from celery import shared_task 
import requests

@shared_task
def get_coin_data(coin):
  url = f'https://api.bithumb.com/public/ticker/{coin}_KRW'
  response = requests.get(url)
  return response.json()