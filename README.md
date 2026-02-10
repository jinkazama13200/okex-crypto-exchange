# OKEx CCXT Price Fetcher

## Overview

The OKEx CCXT Price Fetcher is a project that enables users to fetch real-time cryptocurrency prices from the OKEx exchange using the CCXT library. This project simplifies the process of accessing market data by providing a convenient interface.

## Features
- Real-time price fetching for various cryptocurrencies.
- Supports multiple trading pairs available on OKEx.
- Easy to integrate and use with existing trading systems.

## Requirements
- Python 3.6+
- CCXT library

## Installation
To install the required CCXT library, run:
```bash
pip install ccxt
```

## Usage
```python
import ccxt

# Create an instance of the OKEx exchange
exchange = ccxt.okex()

# Fetch the ticker information for a specific trading pair
ticker = exchange.fetch_ticker('BTC/USDT')
print(ticker)
```

## License
This project is licensed under the MIT License.