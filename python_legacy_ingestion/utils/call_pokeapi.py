#----------------------------------------------------------------
# NOTES TO SELF 
# 
# Here I have defined all the functions I need for this project regarding API calls, in one place.
# The API uses pagination, so I have to iterate across all the pages until there are no more.
#
# Pagination = splitting a large dataset into smaller chunks that can be requested incrementally via an API.
# Many APIs enforce a max limit (usually 100 or 200).
#
# APIs paginate because:
# - Performance (don’t send 100k rows in one response)
# - Memory limits (server + client)
# - Network stability
# - Rate limiting protection
# - Consistency (data may change during fetch)
# - Two main types
#   - Offset-based --> limit + offset
#   - Cursor-based (more modern / scalable) --> ?cursor=abc123
#
# --- denotes in-line notes to self
#----------------------------------------------------------------


"""
Docstrings, Args, Returns here...
"""

import requests
from python_legacy_ingestion.utils.config import base_url


# -----------------------------
# FETCH POKEAPI RESOURCE
# -----------------------------
def fetch_pokeapi_resource(url: str) -> dict:
    """
    Sends a request to the provided endpoint URL, validates the response, and returns the parsed JSON payload.

    Args:
        url: Requires an API endpoint URL as a str.
    Returns:
        Dict: Returns a python dict from a JSON response.
    """

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"[POKEAPI ERROR] Failed to fetch Pokemon data from API url "
            f"| Status: {response.status_code} "
            f"| URL: {url}"
        )
            # --- best practice: a good message is one that tells you exactly why it failed
            # --- best practice: use logger library: DEBUG, INFO, WARNING, ERROR
    
    return response.json()


# -----------------------------
# FETCH POKEMON ENDPOINT
# -----------------------------
def fetch_pokemon_endpoint(endpoint: str, limit: int = 100) -> list:
    """
    Fetches data from a specified endpoint, utilising pagination.

    Args:
        endpoint (int): Specified API endpoint
        limit (int): Defines the number of records returned per API request (page size / batch size per request)
    
    Returns:
        list: Returns a list of dicts from a specified endpoint (each dict includes the name and a URL containing detailed data of that endpoint)
    """
    offset = 0

    all_data = []

    while True:
        # Constructing the url
            # --- limit = number of records returned per API request (page size / batch size per request)
            # --- offset = starting index/position in the dataset for the current request (pagination control)
            # --- pagination = mechanism to retrieve full dataset in chunks using limit + offset (or cursor method)
        url = f"{base_url}/{endpoint}?limit={limit}&offset={offset}"
                
        data = fetch_pokeapi_resource(url)

        results = data["results"]
            # --- specifiying the "results" key within fetch_pokeapi_resource(url) ie response.json()
        
        all_data.extend(results) 
            # --- append adds a single item, extend adds multiple items

        # If no next page -> stop
        if data["next"] is None:
            break

        offset += limit

    return all_data