from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "0-bronze"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)
print(f"Listando os blobs no container: {container_name}")

local_file_name = "exchange_rate_btc_brl_1710115541.json"
upload_file_path = os.path.join("./data/", local_file_name)

blob_client = blob_service_client.get_blob_client(
    container=container_name, blob=f"exchange_rate/{local_file_name}"
)

with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"\nUpload concluído!")
