"""
Main orchestration script (EL only).

Responsibilities:
- Extract data from PokeAPI
- Pass raw JSON to Snowflake service layer

No transformations happen here.
All transformations are handled in dbt.

Pipeline:
Extract → Load (RAW JSON)
"""

from src.utils.pokeapi import get_pokemon_list, get_pokemon_detail
from src.services.snowflake_json_insert import load_raw_json


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    """
    Extract → Load pipeline (no transform)
    """

    print("🚀 Starting RAW Pokemon ingestion pipeline...")

    # 1. Get list of Pokémon
    pokemon_list = get_pokemon_list(limit=100)
    print(f"📦 Found {len(pokemon_list)} Pokémon")

    raw_records = []

    # 2. Fetch full JSON for each Pokémon
    for i, p in enumerate(pokemon_list):

        try:
            raw = get_pokemon_detail(p["url"])
            raw_records.append(raw)

            # Progress logging
            if i % 50 == 0:
                print(f"⏳ Retrieved {i} Pokémon...")

        except Exception as e:
            print(f"❌ Error fetching {p['name']}: {e}")

    print(f"🧱 Collected {len(raw_records)} raw JSON records")

    # 3. Load into Snowflake (delegated to service layer)
    print("❄️ Loading raw data into Snowflake...")
    load_raw_json(raw_records)

    print("🎉 RAW ingestion completed successfully")


# -----------------------------
# TEST PIPELINE
# -----------------------------
def test_load_only():
    """
    Minimal test to validate raw JSON loading
    """

    print("🧪 Test mode: loading raw JSON")

    test_record = {
        "id": 9999,
        "name": "testmon",
        "height": 1,
        "weight": 1,
        "base_experience": 1,
        "types": [{"type": {"name": "normal"}}]
    }

    load_raw_json([test_record])

    print("✅ Test load complete")


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
    # test_load_only()