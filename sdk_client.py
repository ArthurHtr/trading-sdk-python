# sdk_client.py
import requests

class TradingClient:
    def __init__(self, base_url: str, api_key: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    def ping(self):
        url = f"{self.base_url}/api/sdk/ping"
        r = requests.get(url, headers=self._headers())
        print("status:", r.status_code, "body:", r.text)  # debug
        r.raise_for_status()
        return r.json()
