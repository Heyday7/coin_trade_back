import requests

def get_coin_price(ticker):
    url = f'https://api.bithumb.com/public/ticker/{ticker}_KRW'
    response = requests.get(url)
    data = response.json()
    return data