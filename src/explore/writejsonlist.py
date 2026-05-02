import requests
import json
from explore.config import POKEAPI_BASE_URL

url = POKEAPI_BASE_URL

response = requests.get(url)

data = response.json()

with open("resourcelist.json", "w") as f:
    json.dump(data, f, indent=2)