# Poké-Analytics Platform

End-to-end data platform built on PokeAPI (https://pokeapi.co/), simulating real-world data engineering workflows including ingestion, transformation, orchestration, and analytics. The project transforms highly nested Pokémon API data into structured, analytics-ready dimensional models using modern ELT and warehouse design principles.

## Problem Statement

Pokémon data is publicly available through PokeAPI, but it is fragmented across multiple endpoints, highly nested in semi-structured JSON, and not designed for analytical use. Key information such as Pokémon stats, moves, abilities, and types must be retrieved separately and joined manually, making it difficult to query efficiently or perform meaningful analysis.

## Solution

This project builds an end-to-end data platform that ingests data from PokeAPI, transforms it into structured, analytics-ready models. By leveraging a modern data stack including Airbyte, Snowflake, dbt, and Airflow, the platform demonstrates production-style data engineering practices. The final output is a scalable and well-structured data layer designed to power analytics and visualisations for Pokémon-related insights.

## Target Personas

* 'game analysts'
* 'competitive battlers'
* 'Pokémon researchers'
* 'game designers'

## Business Questions

### Pokémon Overview Questions

* Which generation has the most legendary Pokémon?
* What are the heaviest Pokémon?
* Which types have the highest average base experience?
* How many Pokémon exist per type?
* What percentage are dual-type?

### Competitive/Battle Questions

* Which stats correlate most with base experience?
* Which types dominate speed?
* What are the strongest defensive Pokémon?
* Which abilities appear most frequently?

### Game Design Questions
* Are newer generations stronger?
* Did average stats increase over generations?
* Are legendary Pokémon overpowered?

## Architecture

------------*Architecture diagram to be added here* ---------------

## Tech Stack

### **Airbyte (Ingestion)**

* Simplifies API data ingestion without building custom connectors
* Handles pagination, scheduling, and schema detection
* Ideal for rapidly integrating external data sources

### **Snowflake (Data Warehouse)**

* Scalable cloud data warehouse
* Supports semi-structured data (JSON)
* Separates compute and storage
* Industry-standard tool used in modern data stacks

### **dbt (Transformation & Modelling)**

* Transforms raw data into clean, structured models
* Enables modular SQL development
* Built-in testing and documentation
* Encourages best practices (layered architecture, lineage)

### **Apache Airflow (Orchestration)**

* Manages pipeline scheduling and dependencies
* Supports retries, logging, and monitoring
* Enables production-style workflow orchestration

### **Docker (Local Development)**

* Ensures reproducible environments
* Allows all services (Airflow, dbt, etc.) to run locally
* Simplifies onboarding and setup

### **Python & SQL**

* Python → ingestion logic, simulation of dynamic data, orchestration
* SQL → transformations, modelling, analytics

### **GitHub (Version Control)**

* Tracks changes across the project
* Enables collaboration and versioning
* Essential for production-grade workflows

## Data Model

The platform follows a **layered architecture**:

### RAW

* Direct ingestion from PokeAPI
* Minimal transformation
* Stores semi-structured JSON

**Tables:**

* `pokemon_raw`
* `moves_raw`
* `abilities_raw`
* `species_raw`
* `sprites_raw`
* `cries_raw`

### STAGING

* Cleaned and standardised data
* Flattened JSON structures
* Renamed and typed columns

**Tables:**

* `stg_pokemon`
* `stg_pokemon_types`
* `stg_pokemon_abilities`
* `stg_pokemon_moves`
* `stg_pokemon_stats`
* `stg_pokemon_species`
* `stg_pokemon_media`

### MARTS

* Business-ready models using a **star schema**

#### Dimension Tables:

* `dim_pokemon`
* `dim_ability`
* `dim_moves`

#### Fact Tables:

* `fact_pokemon_stats`
* `fact_pokemon_moves`

### Star Schema Benefits

* Optimised for analytical queries
* Simplifies joins and aggregations
* Improves performance in BI tools
* Aligns with industry best practices

## How to Run this Project

### Prerequisites

* Docker
* Docker Compose
* Python 3.10+
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/pokeanalytics-platform.git
cd pokeanalytics-platform
```

### Step 2: Start Services

```bash
docker-compose up -d
```

This will start:

* Airflow
* Supporting services (e.g. scheduler, database)

### Step 3: Configure Airbyte

* Access Airbyte UI
* Set up PokeAPI connector
* Configure destination (Snowflake)

### Step 4: Run dbt Models

```bash
cd dbt
dbt run
dbt test
```

### Step 5: Trigger Airflow DAG

* Open Airflow UI
* Enable and trigger DAG
* Monitor pipeline execution

## Lessons Learned

This project demonstrates several key data engineering and analytics engineering concepts:

### 📌 Data Modelling

* Transforming nested semi-structured API data into relational models
* Flattening arrays and handling one-to-many relationships
* Designing dimensional models and star schemas for analytics
* Building business-focused marts from normalized staging layers

### 📌 ELT & Warehouse Architecture

* Separating RAW, STAGING, and MARTS layers
* Storing raw JSON data for traceability and reprocessing
* Using SQL-based transformations to create analytics-ready datasets
* Applying modern ELT design principles using Snowflake and dbt

### 📌 Data Transformation

* Parsing and flattening nested JSON structures
* Standardising datatypes and naming conventions
* Creating reusable transformation models in dbt
* Managing joins across multiple API endpoints

### 📌 Orchestration

* Coordinating ingestion and transformation workflows
* Managing task dependencies between pipeline stages
* Scheduling and automating data refresh processes

### 📌 Real-World Tradeoffs

* Deciding how much source data to model
* Balancing normalization in staging vs denormalization in marts
* Designing models around analytical use cases rather than source structure
* Keeping the platform scalable while maintaining simplicity

### 📌 Tooling & Architecture

* Integrating APIs, Snowflake, dbt, orchestration, and BI tooling into a cohesive platform
* Understanding the role of each layer in a modern analytics stack
* Building modular and maintainable data pipelines

## 🚀 Future Improvements

* Add incremental loading strategies for API ingestion
* Introduce historical snapshot tracking for slowly changing data
* Expand dimensional models with additional Pokémon endpoints
* Implement automated data quality testing and monitoring
* Add CI/CD pipelines for deployment automation
* Enhance Power BI dashboards and analytical use cases
* Add orchestration monitoring and alerting
* Explore streaming or near real-time ingestion patterns

## Contact

**Author:** Sinan Ozcetin \
**Role:** Senior Analytics / Data Engineer

* LinkedIn: https://www.linkedin.com/in/sinanozcetin/
* GitHub: https://github.com/SinanData26
