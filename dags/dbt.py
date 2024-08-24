from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='POC',
    default_args=default_args,
    description='A simple dbt DAG',
    schedule_interval='@daily',
    start_date=datetime(2023, 8, 24),
    catchup=False,
) as dag:

    # Task to run dbt run
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --profiles-dir C:/Users/ASUS/.dbt --project-dir C:/Users/ASUS/Desktop/snowflake-dbt/dags/airflow_dbt',
    )

 

    dbt_run 
