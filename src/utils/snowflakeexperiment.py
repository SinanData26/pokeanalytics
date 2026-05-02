"""
Snowflake service module (row-by-row insert version).

This version uses standard INSERT statements.
It is simple, easy to understand, but NOT suitable for large-scale loads.

Use only for:
- learning
- small datasets
- debugging pipelines
"""

import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


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


def load_dataframe_row_by_row(df):
    """
    Load DataFrame into Snowflake using row-by-row INSERT statements.

    ⚠️ This is inefficient for large datasets because:
    - Each row is a separate SQL query
    - High network + execution overhead

    Still useful for:
    - learning SQL execution flow
    - small datasets (< few thousand rows)
    """

    conn = get_connection()
    cursor = conn.cursor()

    TABLE = os.getenv("SNOWFLAKE_TABLE")

    try:
        for _, row in df.iterrows():

            cursor.execute(
                f"""
                INSERT INTO {TABLE} (
                    id,
                    name,
                    height,
                    weight,
                    base_experience,
                    types
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    row["id"],
                    row["name"],
                    row["height"],
                    row["weight"],
                    row["base_experience"],
                    row["types"]
                )
            )

        print(f"✅ Inserted {len(df)} rows into {TABLE}")

    except Exception as e:
        print(f"❌ Error during insert: {e}")
        raise

    finally:
        cursor.close()
        conn.close()