import os

from api_requests import ExchangeRateApi
from data_writer import BlobDataWriter, LocalDataWriter
from dotenv import load_dotenv

load_dotenv(".env")

coin_list = ["USD-BRL", "EUR-BRL", "BTC-BRL"]
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "0-bronze"

directory = "./data"

for coin in coin_list:

    requests = ExchangeRateApi(coin=coin)
    file = requests.get_data()
    # writer = LocalDataWriter(coin=coin, json_data=file, directory=directory)
    writer = BlobDataWriter(coin=coin, json_data=file, container_name=container_name, connect_str=connect_str)
    writer.upload_blob()
