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


from python_legacy_ingestion.utils.insert_into_snowflake_table_raw import get_connection
from python_legacy_ingestion.utils.insert_into_snowflake_table_raw import load_raw_json
from python_legacy_ingestion.utils.config import snowflake_table_pokemon

# -----------------------------
# TEST SNOWFLAKE CONNECTION
# -----------------------------
def test_connection():
    """
    Simple test to validate Snowflake connectivity.
    """

    print("Testing Snowflake connection...")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT CURRENT_VERSION()")
        version = cursor.fetchone()
        print(f"✅ Connected to Snowflake: {version[0]}")

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# TEST SNOWFLAKE INSERT
# -----------------------------
def test_insert():
    """
    Minimal test to validate raw JSON insertion into table.
    """

    print("Testing insert into Snowflake table...")

    test_record = {
        "id": 9991,
        "name": "testmon"
    }

    load_raw_json(
        endpoint="test",
        table=snowflake_table_pokemon,
        records=[test_record]
    )
    
    print("✅ Test load complete")


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    #test_connection()
    test_insert()