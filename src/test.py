import requests
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon?limit=10"

response = requests.get(url)
data = response.json()

pokemon = data

df = pd.DataFrame(pokemon)

print (df.head())