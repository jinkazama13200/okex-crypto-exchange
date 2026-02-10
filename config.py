# Configuration settings for OKEx API, trading, and logging

# OKEx API settings
OKEX_API_KEY = 'your_api_key_here'
OKEX_API_SECRET = 'your_api_secret_here'
OKEX_API_PASSPHRASE = 'your_api_passphrase_here'

# Trading settings
 trading_settings = {
    'symbol': 'BTC-USDT',
    'order_size': 0.01,
    'leverage': 10,
    'trade_interval': '1m'
}

# Logging settings
LOGGING_LEVEL = 'DEBUG'
LOG_FILE = 'okex_trader.log'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
