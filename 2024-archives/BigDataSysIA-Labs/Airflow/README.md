<!--StartFragment-->
## Airflow
Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It is used to manage and orchestrate complex workflows or pipelines in data engineering, machine learning, and other automated systems. Airflow is especially popular for managing ETL (Extract, Transform, Load) workflows.

### Key Concepts in Apache Airflow:

DAG (Directed Acyclic Graph): A collection of tasks organized with dependencies and relationships to define the order of execution.

Task: A single unit of work in a DAG, such as running a script or querying a database.

Operator: A template or task that performs a specific function (e.g., BashOperator for running bash commands, PythonOperator for running Python functions).

Task Instance: A specific run of a task; it's an instance of a task.

Scheduler: The component that triggers tasks to run.

Executor: Executes the tasks (e.g., LocalExecutor, CeleryExecutor).

Web UI: A graphical interface to monitor and manage DAGs and tasks.


## Running Airflow in Docker
<https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#>


## Fetching `docker-compose.yaml`

To deploy Airflow on Docker Compose, you should fetch docker-compose.yaml.

From the below link 

<https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml>

Or run curl command:\
`curl -LfO '`[`https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml`](https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml)`'`

This `Docker-compose.yaml ` file contains several service definitions:

- `airflow-scheduler` - The [scheduler](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html) monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

- `airflow-webserver` - The webserver is available at `http://localhost:8080`.

- `airflow-worker` - The worker that executes the tasks given by the scheduler.

- `airflow-triggerer` - The triggerer runs an event loop for deferrable tasks.

- `airflow-init` - The initialization service.

- `postgres` - The database.

- `redis` - [The redis](https://redis.io/) - broker that forwards messages from scheduler to worker.


## Initializing Environment

Before starting Airflow for the first time, you need to prepare your environment, i.e. create the necessary files, directories and initialize the database.

    mkdir -p ./dags ./logs ./plugins ./config


### Setting the right Airflow user

On Linux, the quick-start needs to know your host user id and needs to have group id set to `0`. Otherwise the files created in `dags`, `logs` and `plugins` will be created with `root` user ownership. You have to make sure to configure them for the docker-compose:

Check your user id on terminal using\
`id`
\
then
\
`echo -e "AIRFLOW_UID=$(id -u)" > .env`

#### Add sample .gitignore file 

https://github.com/apache/airflow/blob/main/.gitignore
\
To make sure we don’t push logs & .env files on GitHub
### Update the following in docker-compose.yml
#### Do not load examples
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
#### Additional python package 
`_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- pandas }`
\
This allows to use variables among multiple tasks
`AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'`



#### Change default admin credentials
`_AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow2}`
\
`_AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow2}`


### Initialize the database

On all operating systems, you need to run database migrations and create the first user account. To do this, run.

    docker compose up airflow-init


### Running Airflow

Now you can start all services:\
`docker compose up`


## **Step 1: Set Airflow Variables in the Web UI**

- Navigate to **Admin** > **Variables** in the Airflow Web UI.
- Set the variables `DATABASE_URL` and `API_KEY`.


<!--EndFragment-->
