import requests

BASE_URL = 'https://api.okex.com/api/v5/market/trades'

def fetch_recent_trades(instrument_id):
    try:
        # Send request to fetch recent trades
        response = requests.get(BASE_URL, params={'instId': instrument_id})
        response.raise_for_status()

        # Parse the response JSON
        trades = response.json()['data']
        
        # Print recent trades with timestamp and price
        for trade in trades:
            timestamp = trade['ts']
            price = trade['px']
            print(f'Time: {timestamp}, Price: {price}')
    except Exception as e:
        print(f'Error fetching trades: {e}')

# Example usage
if __name__ == '__main__':
    instrument_id = 'BTC-USDT'  # Replace with desired instrument ID
    fetch_recent_trades(instrument_id)