# Taskflow API Style Version 2

import datetime
from airflow.decorators import dag, task
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
import psycopg2 as db
import pyodbc

@dag(schedule_interval=None, start_date=datetime.datetime(2020, 2, 3), catchup=False, tags=['example'])
def postgres_operator_dag_api():

    # task for extracting data from postgres db and staging it to the local hard drive as pandas dataframe
    # the task returns the filename of the staged pandas dataframe
    @task()
    def extract_stage():
        conn_string="dbname='hkadb1' host='localhost' user='adbith4' password='MyVsP291Klv'"
        conn=db.connect(conn_string)
        sql="SELECT * FROM pet;"
        df=pd.read_sql(sql,con=conn)
        fn='~/staging_area/fromPets_{}.pkl'.format(datetime.datetime.now().timestamp())
        df.to_pickle(fn)
        return fn

    # task reads the staged pandas dataframe from the hard drive and returns the number of rows
    @task()
    def transform(fn):
        df=pd.read_pickle(fn)
        return df.shape[0]

    # task stores the result (number of rows) to our Dataware house (mssql-Server)
    @task()
    def load(number_of_pets: int):
        server = 'localhost'
        database = 'numPets' 
        username = 'sa' 
        password = 'MyVsP291.%Klv' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cursor.execute('INSERT INTO num_pets(NumPets) VALUES (?)',int(number_of_pets))
        cnxn.commit()

    load(transform(extract_stage()))

postgres_operator_dag_api=postgres_operator_dag_api()
