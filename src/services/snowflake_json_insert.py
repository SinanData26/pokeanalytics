"""
Snowflake service module (RAW JSON / VARIANT version).

This module is responsible ONLY for:
- Creating Snowflake connections
- Loading raw JSON data into Snowflake

Design principles:
- No business logic
- No transformations
- Accept raw Python dicts and persist them as JSON

This supports modern ELT architecture:
Python (EL) → Snowflake (RAW) → dbt (T)
"""

import os
import json
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# CONNECTION
# -----------------------------
def get_connection():
    """
    Create and return a Snowflake connection using environment variables.
    """

    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )


# -----------------------------
# RAW JSON LOAD (ROW-BY-ROW)
# -----------------------------
def load_raw_json(records):
    """
    Load raw JSON records into Snowflake VARIANT column.

    Parameters:
        records (list[dict]): List of raw API responses

    Notes:
    - Stores full JSON payload in VARIANT column
    - No transformations applied
    - Row-by-row insert (simple but not scalable)
    """

    conn = get_connection()
    cursor = conn.cursor()

    table = os.getenv("SNOWFLAKE_TABLE_JSON")

    insert_query = f"""
        INSERT INTO {table} (ingest_at, source, raw_data)
        SELECT CURRENT_TIMESTAMP, %s, PARSE_JSON(%s)
    """

    try:
        for record in records:
            cursor.execute(
                insert_query,
                (
                    "pokeapi",
                    json.dumps(record)  # dict → JSON string
                )
            )

        print(f"✅ Inserted {len(records)} raw JSON records into {table}")

    except Exception as e:
        print(f"❌ Error during raw JSON insert: {e}")
        raise

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# TEST FUNCTION
# -----------------------------
def test_connection():
    """
    Simple test to validate Snowflake connectivity.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT CURRENT_VERSION()")
        version = cursor.fetchone()
        print(f"✅ Connected to Snowflake: {version[0]}")

    finally:
        cursor.close()
        conn.close()