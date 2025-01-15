Setup SnowSQL->
    https://docs.snowflake.com/user-guide/snowsql-install-config
    https://developers.snowflake.com/snowsql/

Setup Warehouse, Image repository, and compute pool
    connect to sql either via VScode snowflake extension
    demo.sql

Build the docker image from Dockerfile
    docker build --rm --platform linux/amd64 -t sfedu02-urb63596.registry.snowflakecomputing.com/tutorial_db/data_schema/tutorial_repository/streamlit_image:latest .

Upload the image to the Docker registry in snowflake
    docker login sfedu02-urb63596.registry.snowflakecomputing.com -u cobra

Push docker image to snowfalek regsitry
    docker push sfedu02-urb63596.registry.snowflakecomputing.com/tutorial_db/data_schema/tutorial_repository/streamlit_image:latest

Create service by running services.sql
Get getpoint for service
Grant permissions to test role