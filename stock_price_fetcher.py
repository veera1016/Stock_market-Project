# stock_price_fetcher.py

import requests

def fetch_stock_price(symbol):
    api_key = '3USITZI3NPK3ODAY'
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    price = fetch_stock_price(symbol)
    if price:
        print(f"Current price of {symbol}: {price}")
    else:
        print(f"Failed to fetch price for {symbol}")
