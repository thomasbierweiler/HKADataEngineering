# Style Version 1
# set-up the database connection for airflow
# https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html
"""
CREATE DATABASE hkadb1;
CREATE USER adbith4 WITH PASSWORD 'MyVsP291Klv';
GRANT ALL PRIVILEGES ON DATABASE hkadb1 TO adbith4;
"""
# before starting airflow standalone, set password via
# export AIRFLOW_CONN_POSTGRES_DEFAULT='postgresql://adbith4:MyVsP291Klv@1.1.1.1:5432/hkadb1'
# export AIRFLOW_CONN_POSTGRES_DEFAULT='postgresql://postgres_user:XXXXXXXXXXXX@1.1.1.1:5432/postgresdb?'


# Siehe https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/operators/postgres_operator_howto_guide.html
# install package 
# python3 -m pip install apache-airflow-providers-postgres

import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    catchup=False,
    tags=['example'],
) as dag:
    create_pet_table2 = PostgresOperator(
        task_id="create_pet_table2",
        #postgres_conn_id="postgres_default",
        sql="""
            CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            OWNER VARCHAR NOT NULL);
          """,
    )
    populate_pet_table2 = PostgresOperator(
        task_id="populate_pet_table2",
        #postgres_conn_id="postgres_default",
        sql="""
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Max', 'Dog', '2018-07-05', 'Jane');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Susie', 'Cat', '2019-05-01', 'Phil');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Lester', 'Hamster', '2020-06-23', 'Lily');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Quincy', 'Parrot', '2013-08-11', 'Anne');
            """,
    )
    get_all_pets2 = PostgresOperator(task_id="get_all_pets2", sql="SELECT * FROM pet;")
    get_birth_date2 = PostgresOperator(
        task_id="get_birth_date2",
        #postgres_conn_id="postgres_default",
        sql="""
            SELECT * FROM pet
            WHERE birth_date
            BETWEEN SYMMETRIC DATE '{{ params.begin_date }}' AND DATE '{{ params.end_date }}';
            """,
        params={'begin_date': '2020-01-01', 'end_date': '2020-12-31'},
    )

    create_pet_table2 >> populate_pet_table2 >> get_all_pets2 >> get_birth_date2

"""
if __name__ == "__main__":
    from airflow.utils.state import State

    dag.clear(dag_run_state=State.NONE)
    dag.run()
"""
