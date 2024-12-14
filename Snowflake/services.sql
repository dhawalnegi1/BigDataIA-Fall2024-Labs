USE ROLE test_role;
USE DATABASE tutorial_db;
USE SCHEMA data_schema;
USE WAREHOUSE tutorial_warehouse;
DESCRIBE COMPUTE POOL tutorial_compute_pool;
CREATE SERVICE streamlit_demo
  IN COMPUTE POOL  tutorial_compute_pool
  FROM SPECIFICATION $$
    spec:
        containers:
          - name: streamlit
            image: sfedu02-urb63596.registry.snowflakecomputing.com/tutorial_db/data_schema/tutorial_repository/streamlit_image:latest
            env:
                SNOWFLAKE_WAREHOUSE: TUTORIAL_WAREHOUSE
        endpoints:
          - name: streamlit-endpoint
            port: 8501
            public: true
    serviceRoles:
      - name: app
        endpoints:
          - streamlit-endpoint 
    $$;

SHOW SERVICES IN COMPUTE POOL tutorial_compute_pool;
SELECT system$get_service_status('streamlit_demo');
DESCRIBE SERVICE streamlit_demo;
SHOW ENDPOINTS IN SERVICE streamlit_demo;
GRANT SERVICE ROLE streamlit_demo!app TO ROLE test_role;


drop service streamlit_demo;