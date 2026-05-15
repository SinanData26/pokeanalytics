/*
this is my script to run once in Snowflake to create a table for the pokemon_raw table in the raw layer
*/

CREATE SCHEMA IF NOT EXISTS pokeanalytics.raw; 

// creates pokemon_species_raw table
CREATE OR REPLACE TABLE pokeanalytics.raw.pokemon_species_raw (
    ingestion_id STRING,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source STRING,
    endpoint STRING,
    record_id INT,
    record_name STRING,
    raw_results VARIANT
);

// creates pokemon_raw table
CREATE OR REPLACE TABLE pokeanalytics.raw.pokemon_raw (
    ingestion_id STRING,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source STRING,
    endpoint STRING,
    record_id INT,
    record_name STRING,
    raw_results VARIANT
);

// creates evolution_chain_raw table
CREATE OR REPLACE TABLE pokeanalytics.raw.evolution_chain_raw (
    ingestion_id STRING,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source STRING,
    endpoint STRING,
    record_id INT,
    record_name STRING,
    raw_results VARIANT
);

// creates ability_raw table
CREATE OR REPLACE TABLE pokeanalytics.raw.ability_raw (
    ingestion_id STRING,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source STRING,
    endpoint STRING,
    record_id INT,
    record_name STRING,
    raw_results VARIANT
);

// creates moves_raw table
CREATE OR REPLACE TABLE pokeanalytics.raw.moves_raw (
    ingestion_id STRING,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source STRING,
    endpoint STRING,
    record_id INT,
    record_name STRING,
    raw_results VARIANT
);