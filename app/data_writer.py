import json
import logging
import os
from datetime import datetime

from azure.storage.blob import BlobServiceClient
from pytz import timezone

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class LocalDataWriter:
    def __init__(self, coin: str, json_data: dict, directory: str = "./data") -> None:
        """Initializes the LocalDataWriter with cryptocurrency data.

        Parameters:
        - coin: The name of the cryptocurrency.
        - json_data: The JSON data of the cryptocurrency's exchange rate.
        - directory: The directory where the data file will be saved.
        """
        self.coin = coin
        self.json_data = json_data
        self.directory = directory
        self.filename = self._generate_filename()

    def _generate_filename(self) -> str:
        """Generates a timestamped filename for the cryptocurrency data file.

        Returns:
        - A string representing the filename.
        """
        now_br = datetime.now().astimezone(timezone("America/Sao_Paulo"))
        now_br_formatted = int(now_br.timestamp())
        return f"exchange_rate_{self.coin.lower().replace('-', '_')}_{now_br_formatted}.json"

    def write_to_file(self) -> None:
        """Writes the cryptocurrency's JSON data to a file."""
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        file_path = os.path.join(self.directory, self.filename)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.json_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            logging.error(f"Error writing to {file_path}: {e}")

    def save(self) -> None:
        """Saves the cryptocurrency's JSON data to a file and logs the success."""
        self.write_to_file()
        logger.info(f"File {self.filename} saved successfully in {self.directory}")


class BlobDataWriter:
    def __init__(self, coin: str, json_data: dict, container_name: str, connect_str: str) -> None:
        """Initializes the BlobDataWriter with cryptocurrency data for Azure Blob Storage.

        Parameters:
        - coin: The name of the cryptocurrency.
        - json_data: The JSON data of the cryptocurrency's exchange rate.
        - container_name: The Azure Blob Storage container name.
        - connect_str: The connection string for Azure Blob Storage.
        """
        self.coin = coin
        self.json_data = json_data
        self.container_name = container_name
        self.connect_str = connect_str

    def upload_blob(self) -> None:
        """Uploads the cryptocurrency's JSON data to Azure Blob Storage."""
        blob_service_client = self._get_blob_service_client()
        if blob_service_client:
            self._upload_to_blob(blob_service_client)

    def _get_blob_service_client(self) -> BlobServiceClient or None:
        """Creates and returns a BlobServiceClient instance.

        Returns:
        - A BlobServiceClient instance or None if the connection fails.
        """
        try:
            return BlobServiceClient.from_connection_string(self.connect_str)
        except Exception as err:
            logging.error(f"Error creating BlobServiceClient: {err}")
            return None

    def _upload_to_blob(self, blob_service_client: BlobServiceClient) -> None:
        """Handles the upload of JSON data to the specified Azure Blob Storage blob."""
        blob_path = f"exchange_rate/{self.coin}/{self._generate_filename()}"
        try:
            blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=blob_path)
            data = json.dumps(self.json_data, ensure_ascii=False, indent=4)
            blob_client.upload_blob(data, overwrite=True)
            logging.info("Blob successfully uploaded.")
        except Exception as err:
            logging.error(f"Error uploading to blob: {err}")

    def _generate_filename(self) -> str:
        """Generates a timestamped filename for the blob.

        Returns:
        - A string representing the filename.
        """
        now_br = datetime.now().astimezone(timezone("America/Sao_Paulo"))
        now_br_formatted = int(now_br.timestamp())
        return f"exchange_rate_{self.coin.lower().replace('-', '_')}_{now_br_formatted}.json"
