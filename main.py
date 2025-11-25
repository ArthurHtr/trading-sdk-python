from sdk_client import TradingClient

client = TradingClient(
    base_url="http://localhost:3000",
    api_key="keyRDhQAMthOoFYKqGoBrtJEvuPRCrcXMLeHMjjNdsSYczrKADbLKRaiaRuhwLpiRjP"
)
print(client.ping())
