from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.dates import days_ago


# Default arguments for the DAG
default_args = {
    'start_date': days_ago(0),
    'retries': 1,
}
    
# Define the DAG
dag = DAG(dag_id='simple_pipeline_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False)


def print_hello():
    print("Hello, Airflow! This is a simple Python task.")

with dag:

    # Task 1: Download a file using BashOperator
    download_file = BashOperator(
        task_id='download_file',
        bash_command = 'echo "Hello World"'
        # bash_command='curl -o /tmp/test_file.txt https://example.com/test_file.txt'
    )

    # Task 2: Process the data using PythonOperator (just prints a message)
    python_task = PythonOperator(
        task_id='python_task',
        python_callable=print_hello
    )


    # Task 3: Confirm task completion using BashOperator
    complete_task = BashOperator(
        task_id='completion_message',
        bash_command='echo "All tasks are completed!"'
    )

    # Define the order of execution
    download_file >> python_task >> complete_task
