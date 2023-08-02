import requests
import websockets
import json
from os import getenv
from utils import kafka
from dotenv import load_dotenv

load_dotenv()
api_key = getenv("API_KEY")


def get_fundamentals(symbol: str, exchange: str, filter="") -> dict:
    api_url = f"https://eodhistoricaldata.com/api/fundamentals/{symbol}.{exchange}?api_token={api_key}"
    if filter != "":
        api_url += f"&filter={filter}"
    res = requests.get(api_url)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    return data


def get_live_delayed(symbol: str, exchange: str, filter="") -> dict:
    api_url = f"https://eodhistoricaldata.com/api/real-time/{symbol}.{exchange}?fmt=json&api_token={api_key}"
    if filter != "":
        api_url += f"&s={filter}"
    res = requests.get(api_url)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    return data


async def get_live_socket(symbol: str, exchange: str):
    url = f"wss://ws.eodhistoricaldata.com/ws/us?api_token={api_key}"
    payload = {"action": "subscribe", "symbols": f"{symbol}.{exchange}"}
    try:
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps(payload))
            try:
                while True:
                    message = await websocket.recv()
                    if "status_code" not in message:
                        kafka.produce("stock_prices", message)
            except KeyboardInterrupt:
                await websocket.close()
    except Exception as e:
        print(f"Error: {e}")
