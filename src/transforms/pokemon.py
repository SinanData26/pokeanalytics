"""
All data transformation logic lives here.
No API calls, no database logic.
Just data restructuring.
"""

def transform_pokemon(data: dict) -> dict:
    """
    Convert raw Pokemon JSON into structured record.
    This defines the schema of my raw table.
    """
    
    return{
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"],
        "types": ", ".join([t["type"]["name"] for t in data["types"]])
    }