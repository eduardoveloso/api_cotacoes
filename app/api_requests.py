import logging

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ExchangeRateApi():
    def __init__(self, coin: str) -> None:
        """
        Initializes the exchange_rate_api class with the specified currency code.

        Parameters:
            coin (str): The currency code to fetch the exchange rate for.
        """
        self.coin = coin
        self.base_endpoint = "https://economia.awesomeapi.com.br/json/last"

    def get_data(self) -> dict:
        """
        Fetches the exchange rate data for the specified currency code from AwesomeAPI.

        Returns:
            dict: A dictionary containing the exchange rate data.
        """
        endpoint = f"{self.base_endpoint}/{self.coin}"
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
