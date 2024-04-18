# constants.py
import os

# Base URL for API requests
API_BASE_URL = 'https://api.bitget.com'

# Endpoints for public data
SYMBOLS_ENDPOINT = '/api/spot/v1/public/products'
TICKER_ENDPOINT = '/api/spot/v1/market/ticker'
TRADE_DATA_ENDPOINT = '/api/spot/v1/market/depth'

ORDER_ENDPOINT = '/api/spot/v1/trade/order'
# API credentials (use environment variables)
API_KEY = os.getenv('bg_672142d60b18df7778c39aaa154dc248')
API_SECRET = os.getenv('1f64211fdbf569e24d21f3fc7324155f98adb66fb9e5aaf7e19e75c6a3c5181b')
API_PASSPHRASE = os.getenv('qweasdqwe')


