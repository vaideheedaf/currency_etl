from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import extract_live_rates
from transform import transform_live
from load import load

# Default settings for all tasks
default_args = {
    'owner': 'vaidehi',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False
}

# Define the DAG
with DAG(
    dag_id='currency_exchange_etl',
    description='Hourly ETL pipeline for currency exchange rates',
    default_args=default_args,
    start_date=datetime(2026, 8, 1),
    schedule_interval='@hourly',
    catchup=False,
    tags=['finance', 'etl', 'currency']
) as dag:

    def extract_task(**context):
        data = extract_live_rates()
        context['ti'].xcom_push(key='raw_data', value=data)
        print(f"✅ Extracted {len(data['rates'])} currencies")

    def transform_task(**context):
        raw = context['ti'].xcom_pull(key='raw_data')
        records = transform_live(raw)
        context['ti'].xcom_push(key='records', value=records)
        print(f"✅ Transformed {len(records)} records")

    def load_task(**context):
        records = context['ti'].xcom_pull(key='records')
        load(records)
        print(f"✅ Loaded {len(records)} records")

    # Define tasks
    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_task
    )

    t3 = PythonOperator(
        task_id='load',
        python_callable=load_task
    )

    # Set dependencies
    t1 >> t2 >> t3
