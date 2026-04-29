import requests
from config import POKEAPI_BASE_URL

url = POKEAPI_BASE_URL

response = requests.get(url)

print(response.status_code)
print(response.json())