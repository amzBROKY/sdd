# main.py

import datetime
import logging
import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Dict, List
from utils import get_symbols_data, get_ticker_data, get_actual_trade_data
from typing import Any, Dict, List, Optional
# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s', filename='main.log',
                    filemode='a')
logger_stream = logging.getLogger('STREAM')
logger_stream.setLevel(logging.INFO)
formatter_stream = logging.Formatter("%(name)s [%(asctime)s] %(levelname)s %(message)s")
handler_stream = logging.FileHandler("stream.log", mode='w')
handler_stream.setFormatter(formatter_stream)
logger_stream.addHandler(handler_stream)


def generate_mock_schemas() -> List[Dict[str, Any]]:
    # Generate mock schemas or use hardcoded data
    # For simplicity, let's create two mock schemas
    schema1 = {
        'symbol': 'BTC_USDT',
        'prices': [{'close': 50000}, {'close': 51000}, {'close': 52000}],
        # Add other required keys
    }
    schema2 = {
        'symbol': 'ETH_USDT',
        'prices': [{'close': 3000}, {'close': 3050}, {'close': 3100}],
        # Add other required keys
    }
    return [schema1, schema2]


def process_schema(threshold: float, schema: Dict[str, Any]):
    # Simulate processing of schema
    logger_stream.info(f'Processing schema: {schema["symbol"]}')
    # Simulate trade execution based on schema


def main_process(threshold: float, schemas: List[Dict[str, Any]], max_iterations: int = 100):
    start_time = datetime.datetime.now()
    iteration = 0
    while iteration < max_iterations:
        curr_time = datetime.datetime.now()
        if (curr_time - start_time).total_seconds() < 1:
            time.sleep(1)
            start_time = datetime.datetime.now()

        print(f'Processing schemas at {start_time}...')

        # Use ThreadPoolExecutor to process schemas concurrently
        with ThreadPoolExecutor() as executor:
            process_schema_partial = partial(process_schema, threshold)
            executor.map(process_schema_partial, schemas)

        iteration += 1

    print("Max iterations reached. Exiting main_process.")


if __name__ == '__main__':
    # Run your main program here
    symbols = get_symbols_data()
    print(f'Symbols found: {len(symbols)}')
    tickers = [get_ticker_data(symbol) for symbol in symbols.keys()]  # Assuming symbols is a dict
    actual_trade_data = [get_actual_trade_data(symbol) for symbol in symbols.keys()]

    # Combine tickers and actual trade data
    schemas = []
    for ticker, trade_data in zip(tickers, actual_trade_data):
        schema = {**ticker, **trade_data}
        schemas.append(schema)

    main_process(0.5, schemas)
