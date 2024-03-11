import json
from datetime import datetime
from pytz import timezone
import os
import time


class LocalDataWriter:
    def __init__(self, coin: str, json_data: dict) -> None:
        self.coin = coin

        # Defining date time timezone
        now = datetime.now()
        now_br = now.astimezone(timezone("America/Sao_Paulo"))
        now_br_formatted = int(time.mktime(now_br.timetuple()))
        self.filename = f"exchange_rate_{coin.lower().replace('-','_')}_{now_br_formatted}.json"

        # Writing json file
        if not os.path.exists("data"):
            os.makedirs("./data")

        file_path = f"./data/{self.filename}"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
