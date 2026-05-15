"""
Main orchestration script.

This is the ONLY file that coordinates the pipeline.
Everything else is imported services.

End-to-end ingestion pipeline for Pokémon data from PokeAPI into Snowflake.

Pipeline steps:
1. Fetch all Pokémon via paginated API
2. Retrieve detailed data for each Pokémon
3. Transform raw JSON into structured records
4. Load data into Snowflake using bulk loading (write_pandas)

This script represents a simplified but production-aligned ingestion pattern.
"""

import pandas as pd

from python_legacy_ingestion.utils.call_pokeapi import get_pokemon_list, get_pokemon_detail
from python_legacy_ingestion.transforms.pokemon import transform_pokemon # naming too generic - best practice: should be self-explanitory
from python_legacy_ingestion.prototypes.snowflake_pandas import load_dataframe


# -----------------------------
# MAIN PIPELINE (FULL RUN)
# -----------------------------
def main():
    """
    End-to-end ingestion pipeline:
    Extract → Transform → Load
    """
    
    print("🚀 Starting Pokemon ingestion pipeline...")

    # 1. Get list of Pokemon
    pokemon_list = get_pokemon_list(limit=100) # parameter should probably say "page-size"
    print(f"Found {len(pokemon_list)} Pokemon")

    records = []

    # 2. Loop through each Pokemon
    for i, p in enumerate(pokemon_list):

        try:
            # Fetch detailed record
            raw = get_pokemon_detail(p["url"])
            
            # Transform into structured format
            record = transform_pokemon(raw)
            records.append(record)

            # Progress Logging
            if i % 50 == 0:
                print(f"⏳ Processed {i} Pokemon...")
        
        except Exception as e:
            print(f"❌ Error processing {p['name']}: {e}")


    # 3. Convert to DataFrame
    df = pd.DataFrame(records)

    print(f"🧱 Prepared {len(df)} records")

    # 4. Load into Snowflake
    print("❄️ Loading into Snowflake...")
    
    load_dataframe(df)

    print("🎉 Pipeline completed successfully")


# -----------------------------
# TEST PIPELINE (LOAD ONLY)
# -----------------------------
def test_load_only():
    """
    This function is ONLY for testing Snowflake loading.
    It skips API + transform steps.
    """

    print("🧪 Test mode: loading fake data into Snowflake")

    df = pd.DataFrame([
        {
            "id": 9999,
            "name": "testmon",
            "height": 1,
            "weight": 1,
            "base_experience": 1,
            "types": "normal"
        }
    ])

    load_dataframe(df)

    print("✅ Test load complete")




# -----------------------------
# ENTRY POINT CONTROL
# -----------------------------
if __name__ == "__main__":
    main()
    #test_load_only()