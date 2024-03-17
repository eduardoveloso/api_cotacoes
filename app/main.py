from api_requests import exchange_rate_api
from data_writer import LocalDataWriter

coin_list = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL"
]

directory = "./data"

for coin in coin_list:

    requests = exchange_rate_api(coin=coin)

    file = requests.get_data()

    writer = LocalDataWriter(coin=coin, json_data=file, directory=directory)

    LocalDataWriter(coin=coin, json_data=file)
