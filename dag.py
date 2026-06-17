import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="Nasa_ETL",
    start_date=datetime.datetime(2026, 6, 1),
    schedule="0 14 * * *",
    catchup=False,
) as dag:
    extract_task = BashOperator(
    task_id="extract_nasa_etl",
    bash_command="python /opt/airflow/etl/extract.py"
)

transform_task = BashOperator(
    task_id="transform_nasa_etl",
    bash_command="python /opt/airflow/etl/transform.py"
)

load_task = BashOperator(
    task_id="load_nasa_etl",
    bash_command="python /opt/airflow/etl/load.py"
)
extract_task>>transform_task>>load_task
