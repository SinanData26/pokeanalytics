#----------------------------------------------------------------
# NOTES TO SELF 
# 
#
#
#
#
#
#
#
#
#
#
# --- denotes in-line notes to self
#----------------------------------------------------------------


"""
Orchestration script to ingest Pokemon API endpoint (EL).

"""

from python_legacy_ingestion.utils.config import pokemon_endpoint
from python_legacy_ingestion.utils.config import snowflake_table_pokemon
from python_legacy_ingestion.utils.call_pokeapi import fetch_pokemon_endpoint, fetch_pokeapi_resource
from python_legacy_ingestion.utils.insert_into_snowflake_table_raw import load_raw_json



# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    """
    Extract → Load pipeline
    """

    print("🚀 Starting RAW Pokemon endpoint ingestion pipeline...")

    # Get list of all Pokémon names & URLs
    pokemon_list = fetch_pokemon_endpoint(endpoint=pokemon_endpoint, limit=100)
    
    print(f"📦 Found {len(pokemon_list)} Pokémon")

    raw_records = []

    # Fetch full JSON for each Pokémon
    for i, p in enumerate(pokemon_list):

        try:
            raw_pokemon_details = fetch_pokeapi_resource(p["url"])
            raw_records.append(raw_pokemon_details)

            # Progress logging
            if i % 50 == 0:
                print(f"⏳ Retrieved {i} Pokémon...")

        except Exception as e:
            print(f"❌ Error fetching {p['name']}: {e}")

    print(f"🧱 Collected {len(raw_records)} raw JSON records")

    # Load into Snowflake RAW table
    print("❄️ Loading raw data into Snowflake...")
    
    load_raw_json(endpoint=pokemon_endpoint, table=snowflake_table_pokemon, records=raw_records)

    print("🎉 RAW ingestion completed successfully")



# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()