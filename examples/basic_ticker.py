import requests

def fetch_ticker(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    # Fetch BTC/USDT ticker
    btc_usdt = fetch_ticker('BTCUSDT')
    print('BTC/USDT:', btc_usdt)
    
    # Fetch multiple trading pairs
    pairs = ['ETHUSDT', 'LTCUSDT', 'XRPUSDT']
    for pair in pairs:
        ticker = fetch_ticker(pair)
        print(f'{pair}:', ticker)