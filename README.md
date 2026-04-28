# Poké-Analytics Platform

End-to-end data platform built on PokeAPI, simulating real-world data engineering workflows including ingestion, transformation, orchestration, and analytics.  The project combines static Pokémon data with dynamically generated datasets to demonstrate incremental processing, data modelling, and production-style pipeline design.

## Problem Statement

Pokémon data is publicly available through PokeAPI, but it is fragmented across multiple endpoints, highly nested in semi-structured JSON, and not designed for analytical use. Key information such as Pokémon stats, moves, abilities, and types must be retrieved separately and joined manually, making it difficult to query efficiently or perform meaningful analysis. Additionally, the dataset lacks historical tracking and dynamic updates, limiting the ability to analyse trends over time or support more advanced use cases such as team optimisation or gameplay insights.

## Solution

This project builds an end-to-end data platform that ingests data from PokeAPI, transforms it into structured, analytics-ready models, and enriches it with simulated dynamic datasets to enable time-based analysis. By leveraging a modern data stack including Airbyte, Snowflake, dbt, and Airflow, the platform demonstrates production-style data engineering practices such as incremental processing, data modelling, orchestration, and data quality testing. The final output is a scalable and well-structured data layer designed to power analytics and visualisations for Pokémon-related insights.

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

### RAW (Bronze)

* Direct ingestion from PokeAPI
* Minimal transformation
* Stores semi-structured JSON

**Examples:**

* `pokemon_raw`
* `moves_raw`
* `abilities_raw`

### STAGING (Silver)

* Cleaned and standardised data
* Flattened JSON structures
* Renamed and typed columns

**Examples:**

* `stg_pokemon`
* `stg_moves`
* `stg_types`

### MARTS (Gold)

* Business-ready models using a **star schema**

#### Dimension Tables:

* `dim_pokemon`
* `dim_type`
* `dim_ability`

#### Fact Tables:

* `fact_pokemon_stats`
* `fact_pokemon_moves`
* `fact_battles` *(simulated dynamic data)*

#### Bridge Tables:

* `bridge_pokemon_types` (many-to-many relationships)

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

This project demonstrates several key data engineering concepts:

### 📌 Data Modelling

* Designing scalable schemas from nested API data
* Handling many-to-many relationships
* Building star schemas for analytics

### 📌 Orchestration

* Managing dependencies between ingestion and transformation
* Implementing retries and failure handling
* Scheduling pipelines effectively

### 📌 Incremental Processing

* Avoiding full reloads
* Processing only new or updated data
* Designing idempotent pipelines

### 📌 Real-World Tradeoffs

* Handling static vs dynamic datasets
* Deciding what data to store vs reference (e.g. media URLs)
* Balancing simplicity vs scalability

### 📌 Tooling & Architecture

* Integrating multiple tools into one cohesive system
* Understanding the role of each component in the data stack

## 🚀 Future Improvements

* Add real-time data ingestion
* Enhance battle simulation logic
* Implement CI/CD pipelines
* Add data quality monitoring
* Expand BI dashboards

## Contact

**Author:** Sinan Ozcetin \
**Role:** Senior Analytics / Data Engineer

* LinkedIn: https://www.linkedin.com/in/sinanozcetin/
* GitHub: https://github.com/SinanData26
