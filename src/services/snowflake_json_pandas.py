"""
Snowflake service module (write_pandas / bulk load version).

This version uses write_pandas for efficient bulk loading.

Key idea:
- Convert dict → JSON string in pandas
- Load as STRING
- Cast to VARIANT inside Snowflake

This is MUCH more scalable than row-by-row inserts.
"""

import os
import json
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# CONNECTION
# -----------------------------
def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )


# -----------------------------
# RAW JSON LOAD (BULK)
# -----------------------------
def load_raw_json(records):
    """
    Bulk load raw JSON into Snowflake using write_pandas.

    Steps:
    1. Convert dict → JSON string
    2. Load into temporary table
    3. Insert into final table with PARSE_JSON
    """

    conn = get_connection()
    cursor = conn.cursor()

    target_table = os.getenv("SNOWFLAKE_TABLE_JSON")
    temp_table = f"{target_table}_temp"

    try:
        # -----------------------------
        # 1. Prepare DataFrame
        # -----------------------------
        df = pd.DataFrame({
            "raw_data": [json.dumps(r) for r in records],
            "source": ["pokeapi"] * len(records)
        })

        # -----------------------------
        # 2. Create temp table
        # -----------------------------
        cursor.execute(f"""
            CREATE OR REPLACE TEMP TABLE {temp_table} (
                raw_data STRING,
                source STRING
            )
        """)

        # -----------------------------
        # 3. Bulk load into temp table
        # -----------------------------
        success, nchunks, nrows, _ = write_pandas(
            conn,
            df,
            temp_table
        )

        if not success:
            raise Exception("write_pandas failed")

        print(f"📦 Bulk loaded {nrows} rows into temp table")

        # -----------------------------
        # 4. Insert into final table (cast to VARIANT)
        # -----------------------------
        cursor.execute(f"""
            INSERT INTO {target_table} (ingest_at, source, raw_data)
            SELECT
                CURRENT_TIMESTAMP,
                source,
                PARSE_JSON(raw_data)
            FROM {temp_table}
        """)

        print(f"✅ Inserted {nrows} rows into {target_table}")

    except Exception as e:
        print(f"❌ Error during bulk load: {e}")
        raise

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# TEST FUNCTION
# -----------------------------
def test_connection():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT CURRENT_VERSION()")
        print(f"✅ Connected to Snowflake: {cursor.fetchone()[0]}")
    finally:
        cursor.close()
        conn.close()