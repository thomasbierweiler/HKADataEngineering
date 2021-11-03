# Source: Paul Crickard, page 92ff.

import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

import pandas as pd
import psycopg2 as db

# create database table pet
def create_table():
    conn_string="dbname='hkadb1' host='localhost' user='adbith4' password='MyVsP291Klv'"
    conn=db.connect(conn_string)
    sql="""
            CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            OWNER VARCHAR NOT NULL);
          """
    conn.cursor().execute(sql)
    conn.commit()

# insert values into the database table
def populate_table():
    conn_string="dbname='hkadb1' host='localhost' user='adbith4' password='MyVsP291Klv'"
    conn=db.connect(conn_string)
    sql="""
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Max', 'Dog', '2018-07-05', 'Jane');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Susie', 'Cat', '2019-05-01', 'Phil');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Lester', 'Hamster', '2020-06-23', 'Lily');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)
            VALUES ( 'Quincy', 'Parrot', '2013-08-11', 'Anne');
            """
    conn.cursor().execute(sql)
    conn.commit()

# select all data from the database table
def select_data():
    conn_string="dbname='hkadb1' host='localhost' user='adbith4' password='MyVsP291Klv'"
    conn=db.connect(conn_string)
    sql="SELECT * FROM pet;"
    df=pd.read_sql(sql,conn)
    df.to_csv('pet_data.csv')

# select pets with certain birth dates
def get_date():
    conn_string="dbname='hkadb1' host='localhost' user='adbith4' password='MyVsP291Klv'"
    conn=db.connect(conn_string)
    sql="""
            SELECT * FROM pet
            WHERE birth_date
            BETWEEN SYMMETRIC DATE '2020-01-01' AND DATE '2020-12-31';
            """
    df=pd.read_sql(sql,conn)
    df.to_csv('pet_data_data.csv')

default_args = {
    'owner': 'thomasbierweiler',
    'start_date': dt.datetime(2021,4,2),
    'retries': 1,
    'retry_delay': dt.timedelta(seconds=10),
}
with DAG('access_postgres_pythonoperator',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    tags=['example'],
) as dag:
    create_pet_table = PythonOperator(
        task_id="create_pet_table",
        python_callable=create_table
    )
    populate_pet_table = PythonOperator(
        task_id="populate_pet_table",
        python_callable=populate_table
    )
    get_all_pets = PythonOperator(
        task_id="get_all_pets",
        python_callable=select_data
    )
    get_birth_date = PythonOperator(
        task_id="get_birth_date",
        python_callable=get_date
    )

    create_pet_table >> populate_pet_table >> get_all_pets >> get_birth_date
