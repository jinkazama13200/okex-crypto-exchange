import ccxt

class OKExClient:
    def __init__(self, api_key, secret, password):
        self.exchange = ccxt.okex({
            'apiKey': api_key,
            'secret': secret,
            'password': password,
        })

    def fetch_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)

    def fetch_order_book(self, symbol):
        return self.exchange.fetch_order_book(symbol)

    def fetch_trades(self, symbol):
        return self.exchange.fetch_trades(symbol)

    def fetch_ohlcv(self, symbol, timeframe='1m'):
        return self.exchange.fetch_ohlcv(symbol, timeframe)

    def fetch_balance(self):
        return self.exchange.fetch_balance()

    def place_order(self, symbol, order_type, side, amount, price=None, params={}):
        return self.exchange.create_order(symbol, order_type, side, amount, price, params)