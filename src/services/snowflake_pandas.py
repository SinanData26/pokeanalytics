"""
Handles Snowflake connection and loading logic, using write_pandas.
"""

import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """
    Create Snowflake connection using environment variables.
    """

    return snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        password = os.getenv("SNOWFLAKE_PASSWORD"),
        account = os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
        database = os.getenv("SNOWFLAKE_DATABASE"),
        schema = os.getenv("SNOWFLAKE_SCHEMA")
    )

def load_dataframe(df: pd.DataFrame):
    """
    Bulk load DataFrame into Snowflake using write_pandas.

    This is the recommended approach for ingestion workloads.
    """

    conn = get_connection()

    try:
        # Normalize column names to match Snowflake schema
        df.columns = [c.upper() for c in df.columns]

        # -----------------------------
        # DEBUG CHECK (TEMPORARY)
        # -----------------------------
        print("DB:", os.getenv("SNOWFLAKE_DATABASE"))
        print("SCHEMA:", os.getenv("SNOWFLAKE_SCHEMA"))
        print("TABLE:", os.getenv("SNOWFLAKE_TABLE"))

        # -----------------------------
        # ACTUAL LOAD
        # -----------------------------
        success, nchunks, nrows, _= write_pandas(
            conn=conn, 
            df=df,
            table_name="POKEMON_RAW",
            schema="RAW"
        )

        if success:
            print(f"✅ Loaded {nrows} rows in {nchunks} chunk(s)")
        else:
            print("❌ Load failed")
        
    finally:
        conn.close()