import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime, timedelta
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator


from scripts.fetch_contests import fetch_contests
from scripts.transformation import transform
from scripts.load_to_db import load_to_db


# Default arguments for the DAG
default_args = {
    'owner': 'Youssef',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 7),
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}


# Define the DAG
with DAG(
    dag_id ='contest_etl_dag',
    default_args=default_args,
    description='A simple ETL DAG for Codeforces contests',
    schedule_interval='@daily'
) as dag:
    Extract_data = PythonOperator(
        task_id='fetch_contests',
        python_callable=fetch_contests,
    )

    Transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=transform,
        op_kwargs={'data': 'data/contests.csv'},
    )

    Load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_to_db,
        op_kwargs={'data': 'data/contests_transformed.csv'},
    )


Extract_data >> Transform_data >> Load_data