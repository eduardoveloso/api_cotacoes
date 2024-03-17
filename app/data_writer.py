import json
from datetime import datetime
from pytz import timezone
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

load_dotenv(".env")


class LocalDataWriter:
    def __init__(self, coin: str, json_data: dict, directory: str = "./data") -> None:
        self.coin = coin
        self.json_data = json_data
        self.directory = directory
        self.filename = self.generate_filename()

    def generate_filename(self) -> str:
        now_br = datetime.now().astimezone(timezone("America/Sao_Paulo"))
        now_br_formatted = int(now_br.timestamp())
        return f"exchange_rate_{self.coin.lower().replace('-', '_')}_{now_br_formatted}.json"

    def write_to_file(self) -> None:
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        file_path = os.path.join(self.directory, self.filename)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.json_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error writing to {file_path}: {e}")

    def save(self) -> None:
        self.write_to_file()
        logger.info(f"File {self.filename} saved successfully in {self.directory}")


class BlobDataWriter:

    def __init__(self, coin:str, json_data: dict) -> None:
        self.coin=coin

    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = "0-bronze"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)
