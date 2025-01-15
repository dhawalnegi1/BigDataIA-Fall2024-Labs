from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.dates import days_ago
import os
from dotenv import load_dotenv
from datetime import timedelta

# Default arguments for the DAG
default_args = {
    'start_date': days_ago(0),
    'retries': 1,
}
    
# Define the DAG
dag = DAG(
    dag_id='access_env_variables',
    default_args=default_args,
    schedule='0 0 * * *',
    dagrun_timeout= timedelta(minutes =60),
    catchup=False)



#using load_dotenv()
load_dotenv()
database_url = os.getenv('OPENAI_KEY')
api_key = os.getenv('API_KEY')

# Define the Python function
def print_env_vars(**kwargs):
    print(f"Database URL: {database_url}")
    print(f"API Key: {api_key}")

with dag:

    python_task = PythonOperator(
        task_id='display_env_var',
        python_callable=print_env_vars,
        provide_context = True
    )