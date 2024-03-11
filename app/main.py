from api_requests import exchange_rate_api
from data_writer import LocalDataWriter

coin_list = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL"
]

for coin in coin_list:

    requests = exchange_rate_api(coin=coin)

    file = requests.get_data()

    LocalDataWriter(coin=coin, json_data=file)
