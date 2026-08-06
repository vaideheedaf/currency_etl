# 💱 Currency & Cryptocurrency ETL Pipeline

## Overview

This project is an automated **ETL (Extract, Transform, Load) pipeline** that collects live currency exchange rates and cryptocurrency prices every hour, transforms the data, and stores it in a PostgreSQL database for historical analysis.

The workflow is orchestrated using **Apache Airflow**, enabling fully automated hourly data collection.

## Features

* 📈 Tracks 10 global currencies
* ₿ Tracks 5 cryptocurrencies
* ⏰ Automated hourly data collection
* 🗄️ Stores historical data in PostgreSQL
* 🔄 ETL workflow managed by Apache Airflow
* ☁️ Designed for future AWS deployment

## Tech Stack

* **Python** – ETL pipeline
* **Apache Airflow** – Workflow scheduling
* **PostgreSQL** – Data storage
* **Frankfurter API** – Currency exchange rates
* **CoinGecko API** – Cryptocurrency prices

## Project Workflow

1. **Extract** – Fetch live data from Frankfurter and CoinGecko APIs.
2. **Transform** – Clean, structure, and timestamp the data.
3. **Load** – Store the processed data in PostgreSQL.
4. **Schedule** – Run the pipeline automatically every hour using Airflow.

## Future Enhancements

* Deploy on AWS
* Add dashboards (Power BI/Tableau)
* Integrate Docker
* Implement data quality checks

