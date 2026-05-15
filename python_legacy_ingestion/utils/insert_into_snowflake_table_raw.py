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
Snowflake service module (RAW JSON / VARIANT version).

This module is responsible for:
- Creating Snowflake connections
- Loading raw JSON data into Snowflake

This supports modern ELT architecture:
Python (EL) → Snowflake (RAW)
"""

import os
import json
import uuid
from python_legacy_ingestion.utils.config import base_url
from python_legacy_ingestion.utils.config import pokemon_endpoint
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
def load_raw_json(endpoint: str, table: str, records):
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
    
    insert_query = f"""
        INSERT INTO {table} 
            (ingestion_id, ingested_at, source, endpoint, record_id, record_name, raw_results)
        SELECT 
            %s, CURRENT_TIMESTAMP, %s, %s, %s, %s, PARSE_JSON(%s)
    """

    ingestion_id = str(uuid.uuid4())

    try:
        for record in records:
            
            record_id = record["id"]
            record_name = record["name"]

            cursor.execute(
                insert_query,
                (
                    ingestion_id,
                    base_url,
                    endpoint,
                    record_id,
                    record_name,
                    json.dumps(record)  # dict → JSON string
                )
            )

        print(f"✅ Inserted {len(records)} raw JSON record(s) into {table}")
        print(f"📦 ingestion_id: {ingestion_id}")

    except Exception as e:
        print(f"❌ Error during raw JSON insert: {e}")
        raise

    finally:
        cursor.close()
        conn.close()