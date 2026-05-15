import requests
import json
from explore.config import POKEAPI_BASE_URL

url = "https://pokeapi.co/api/v2/pokemon?limit=10"

response = requests.get(url)

# print(response.status_code)

data = response.json()

# print(json.dumps(data, indent=2))

pokemon_list = data["results"]

for p in pokemon_list:
    detail_url = p["url"]
    detail_response = requests.get(detail_url)
    detail_data = detail_response.json()
    
    print(json.dumps(detail_data, indent=2))
    break