USE ROLE ACCOUNTADMIN;

CREATE ROLE test_role;

CREATE DATABASE IF NOT EXISTS tutorial_db;
GRANT OWNERSHIP ON DATABASE tutorial_db TO ROLE test_role COPY CURRENT GRANTS;

CREATE OR REPLACE WAREHOUSE tutorial_warehouse WITH
  WAREHOUSE_SIZE='X-SMALL';
GRANT USAGE ON WAREHOUSE tutorial_warehouse TO ROLE test_role;

GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE test_role;

CREATE COMPUTE POOL tutorial_compute_pool
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS;
GRANT USAGE, MONITOR ON COMPUTE POOL tutorial_compute_pool TO ROLE test_role;

GRANT ROLE test_role TO USER cobra;

USE ROLE test_role;
USE DATABASE tutorial_db;
USE WAREHOUSE tutorial_warehouse;
CREATE SCHEMA IF NOT EXISTS data_schema;
CREATE IMAGE REPOSITORY IF NOT EXISTS tutorial_repository;
CREATE STAGE IF NOT EXISTS tutorial_stage
  DIRECTORY = ( ENABLE = true );
SHOW COMPUTE POOLS;
SHOW WAREHOUSES;
SHOW IMAGE REPOSITORIES;
SHOW STAGES;


drop stage tutorial_stage;
drop image repository tutorial_repository;
drop warehouse tutorial_warehouse;
drop database tutorial_db;
drop role test_role;
drop compute pool tutorial_compute_pool;
