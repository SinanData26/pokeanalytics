"""
Fetch all Pokémon using pagination.

The PokeAPI returns results in pages.
We iterate until there are no more pages.

Args:
    limit (int): Number of records per API call (max ~100)

Returns:
    list: List of Pokémon metadata (name + detail URL)

This is my reusable API client logic, which handles the API call
"""

import requests
from src.utils.config import BASE_URL

def get_pokemon_list(limit: int = 100) -> list:
    """
    Fetch all Pokemon  metadata using pagination.
    Returns name + URL for detail calls.
    Args:
        Limit: this is the page size
    """
    
    all_pokemon = []
    offset = 0

    while True:
        # Constructing the url
        url = f"{BASE_URL}?limit={limit}&offset={offset}"
        response = requests.get(url)
        
        # Including exception handling
        if response.status_code != 200:
            raise Exception(f"Failed to fetch Pokémon list: {response.status_code}")
    
        data = response.json()

        results = data["results"]
        all_pokemon.extend(results)

        # If no next page -> stop
        if data["next"] is None:
            break

        offset += limit

    return all_pokemon


def get_pokemon_detail(url: str) -> dict:
    """
    Fetch detailed Pokemon data from a given URL
    """

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch Pokemon detail: {response.status_code}")
    
    return response.json()