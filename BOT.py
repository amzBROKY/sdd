import websocket
import json
import threading
import time
import hashlib
import hmac
from constants import API_BASE_URL, API_KEY, API_SECRET, API_PASSPHRASE

# Define your WebSocket URL
websocket_url = "wss://csocketapi.bitget.com/ws/v1"

# Define your trading parameters
symbol = "BTCUSDT"
demo_trade_amount = 0.001
demo_trade_side = "buy"  # or "sell"

def generate_signature(timestamp):
    """
    Generate the signature for Bitget authentication.
    """
    message = timestamp + "GET/ws/v1"
    signature = hmac.new(API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()
    return signature


def on_message(ws, message):
    """
    Define what to do when a message is received from the WebSocket server.
    """
    print("Received message:", message)
    # Handle the message according to your trading strategy


def on_error(ws, error):
    """
    Define what to do when an error occurs with the WebSocket connection.
    """
    print("Error:", error)


def on_close(ws):
    """
    Define what to do when the WebSocket connection is closed.
    """
    print("WebSocket closed")


def on_open(ws):
    """
    Define what to do when the WebSocket connection is opened.
    """
    print("WebSocket opened")
    # Perform authentication
    timestamp = str(int(time.time()))
    signature = generate_signature(timestamp)
    auth_data = {
        "op": "login",
        "args": {
            "apiKey": API_KEY,
            "passphrase": API_PASSPHRASE,
            "timestamp": timestamp,
            "sign": signature
        }
    }
    ws.send(json.dumps(auth_data))


def send_demo_trade(ws):
    """
    Send a demo trade request.
    """
    trade_request = {
        "op": "order",
        "args": {
            "symbol": symbol,
            "type": "limit",
            "side": demo_trade_side,
            "price": 50000,  # Example price, adjust according to your strategy
            "size": demo_trade_amount
        }
    }
    ws.send(json.dumps(trade_request))


def start_websocket():
    """
    Start the WebSocket connection and run the trading application.
    """
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    # Start a thread to send demo trade requests periodically
    threading.Thread(target=send_demo_trades_periodically, args=(ws,)).start()

    ws.run_forever()


def send_demo_trades_periodically(ws):
    """
    Send demo trade requests periodically.
    """
    while True:
        send_demo_trade(ws)
        time.sleep(10)  # Adjust the interval as needed


if __name__ == "__main__":
    start_websocket()
