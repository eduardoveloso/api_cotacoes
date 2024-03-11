import requests

moeda = "USD-BRL"

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}/"


r = requests.get(url)
print(r.text)
