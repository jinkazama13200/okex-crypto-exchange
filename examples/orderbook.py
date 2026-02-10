import requests
import json

def fetch_order_book(symbol):
    url = f'https://api.okex.com/api/v5/market/books?instId={symbol}&size=5'
    response = requests.get(url)
    return response.json()


def display_order_book(order_book):
    bids = order_book['data'][0]['bids']
    asks = order_book['data'][0]['asks']
    print("Order Book:")
    print("Bids:")
    for bid in bids:
        print(f"Price: {bid[0]}, Quantity: {bid[1]}")
    print("Asks:")
    for ask in asks:
        print(f"Price: {ask[0]}, Quantity: {ask[1]}")
    bid_price = float(bids[0][0])
    ask_price = float(asks[0][0])
    spread = ask_price - bid_price
    print(f"Bid/Ask Spread: {spread}")


if __name__ == '__main__':
    symbol = 'BTC-USDT'
    order_book = fetch_order_book(symbol)
    display_order_book(order_book)