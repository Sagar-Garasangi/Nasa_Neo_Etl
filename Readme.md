# NASA Near-Earth Object (NEO) ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline that retrieves Near-Earth Object (NEO) data from NASA's NeoWs API, processes and transforms the data, and loads it into a MySQL database for analysis and reporting.

The project was built to practice real-world Data Engineering concepts including API integration, data transformation, relational database loading, Docker containerization, and incremental data ingestion design.

---

## Architecture

NASA NeoWs API → Extract → Transform → Load → MySQL

---

## Features

* Extracts asteroid data from NASA NeoWs API
* Handles nested JSON API responses
* Transforms raw data into structured datasets
* Loads processed data into MySQL
* Modular ETL architecture (Extract, Transform, Load)
* Dockerized application
* Docker Compose setup for ETL and MySQL services
* Designed for future incremental loading support

---

## Tech Stack

* Python
* Pandas
* Requests
* MySQL
* Docker
* Docker Compose
* Git

---

## Project Structure

```text
nasa_etl/
│
├── extract.py
├── transform.py
├── load.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── raw/
├── transformed/
└── README.md
```

---

## ETL Workflow

### Extract

* Connects to NASA NeoWs API
* Retrieves Near-Earth Object data
* Stores raw responses for processing

### Transform

* Flattens nested JSON structures
* Cleans and standardizes fields
* Converts raw API data into structured tabular format

### Load

* Creates database-ready datasets
* Loads processed records into MySQL
* Supports reusable loading logic

---

## Future Improvements

* Incremental loading using metadata tracking
* Apache Airflow orchestration
* Data quality validation checks
* Cloud deployment
* Automated scheduling and monitoring

---

## Learning Outcomes

Through this project I practiced:

* API data extraction
* JSON processing
* Data transformation with Pandas
* Database loading strategies
* Docker containerization
* ETL pipeline design
* Data Engineering workflows

```
```
