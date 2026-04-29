import requests
import json
from config import POKEAPI_BASE_URL

url = POKEAPI_BASE_URL

response = requests.get(url)

print(response.status_code)

data = response.json()

print(json.dumps(data, indent=2))