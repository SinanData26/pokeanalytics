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
    break

print("Name:")
print(detail_data["name"])

print("Stats:")
for stat in detail_data["stats"]:
    print(stat["stat"]["name"], stat["base_stat"])

print("Typing:")
for type in detail_data["types"]: 
    print(type["type"]["name"])