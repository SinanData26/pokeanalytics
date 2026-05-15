#----------------------------------------------------------------
# NOTES TO SELF 
# 
# here I set all my variables to be use across my scripts, 
# for example: contruct URLs to call endpoints
#
#
# --- denotes in-line notes to self
#----------------------------------------------------------------

"""
Docstring: This is where you can describe a module, function, class, or method. 
Unlike regular comments, docstrings are stored as metadata and can be accessed using the __doc__ attribute.

Args:
    parameter (format): describe input parameter
Returns:
    output: describe output

"""

# PokeAPI Base URL
base_url = "https://pokeapi.co/api/v2"

# Pokemon Species endpoint
species_endpoint = "pokemon_species"

# Pokemon endpoint
pokemon_endpoint = "pokemon"

# Evolution Chain endpoint
evolution_endpoint = "evolution_chain"

# Moves endpoint
move_endpoint = "move"

# Abilities endpoint
ability_endpoint = "ability"

# Snowflake target tables
snowflake_table_species = "pokemon_species_raw"
snowflake_table_pokemon = "pokemon_raw"
snowflake_table_evo = "evolution_chain_raw"
snowflake_table_abilities = "ability_raw"
snowflake_table_moves = "moves_raw"