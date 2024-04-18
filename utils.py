# api_utils.py
import requests
from typing import Any, Dict, List, Optional

from constants import API_BASE_URL


def call_api(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = API_BASE_URL + endpoint
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return {}


def get_symbols_data() -> Dict[str, Any]:
    endpoint = '/api/spot/v1/public/products'
    return call_api(endpoint)


def get_ticker_data(symbol: str) -> Dict[str, Any]:
    endpoint = '/api/spot/v1/market/ticker'
    params = {'symbol': symbol}
    return call_api(endpoint, params)


def get_actual_trade_data(symbol: str) -> Dict[str, Any]:
    endpoint = '/api/spot/v1/market/depth'
    params = {'symbol': f'{symbol}_SPBL', 'type': 'step0', 'limit': 2}
    return call_api(endpoint, params)
