/*
this is my script to run once in Snowflake 
to create a table for the raw layer
*/

CREATE SCHEMA IF NOT EXISTS pokeanalytics.raw; 

CREATE TABLE IF NOT EXISTS pokeanalytics.raw.pokemon_raw (
    id INTEGER,
    name STRING,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER,
    types STRING
);