import logging
import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class exchange_rate_api():
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.base_endpoint = "https://economia.awesomeapi.com.br/json/last"

    def get_data(self) -> dict:
        endpoint = f"{self.base_endpoint}/{self.coin}"
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
