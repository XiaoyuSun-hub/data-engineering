import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

default_args = {
 'owner': 'xiaoyusun',
 'start_date': dt.datetime(2023, 5, 30),
 'retries': 1,
 'retry_delay': dt.timedelta(minutes=5),
}

def queryPostgresql():
#  conn_string="dbname='postgres' host='{hostname}.local' user='postgres' password='postgres'"
 conn_string="dbname='postgres' host='172.24.192.1' user='postgres' password='postgres'"
 conn=db.connect(conn_string)
 df=pd.read_sql("select name,city from users",conn)
 df.to_csv('postgresqldata.csv')
 print("-------Data Saved------")

 #create the Elasticsearch object connecting to localhost. 
 # Then, read the CSV from the previous task into a DataFrame, 
def insertElasticsearch():
 es = Elasticsearch() 
 df=pd.read_csv('postgresqldata.csv')
  # iterate through the DataFrame, converting each row into JSON, and insert the data using the index method
 for i,r in df.iterrows():
    doc=r.to_json()
    res=es.index(index="frompostgresql", doc_type="doc",body=doc)
    print(res)


with DAG('MyDBdag',
 default_args=default_args,
 schedule_interval=timedelta(minutes=5), 
 # '0 * * * *',
 ) as dag:
 getData = PythonOperator(task_id='QueryPostgreSQL', python_callable=queryPostgresql)
 
 insertData = PythonOperator (task_id='InsertDataElasticsearch', python_callable=insertElasticsearch)
# The getData task will be upstream and the insertData task downstream
getData >> insertData


