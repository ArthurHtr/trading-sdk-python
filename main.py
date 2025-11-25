# main.py
 
from config_local import BASE_URL, API_KEY
from sdk_client import TradingClient


client = TradingClient(
    base_url=BASE_URL,
    api_key=API_KEY
)

print(client.ping())
