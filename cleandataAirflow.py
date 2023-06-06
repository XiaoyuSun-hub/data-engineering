import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
default_args = {
    'owner': 'xiaoyusun',
    'start_date': dt.datetime(2023, 5, 31),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

#  drop the region ID, convert the columns to lowercase, and change the started_at field to a datetime data type


def cleanScooter():
    df = pd.read_csv('/c/Users/zhushu/airflow/dags/scooter.csv')
    df.drop(columns=['region_id'], inplace=True)
    df.columns = [x.lower() for x in df.columns]
    df['started_at'] = pd.to_datetime(df['started_at'],
                                      format='%m/%d/%Y %H:%M')
    df.to_csv('cleanscooter.csv')
# read in the cleaned data and filter based on a start and end date.


def filterData():
    df = pd.read_csv('cleanscooter.csv')
    fromd = '2019-05-23'
    tod = '2019-06-03'
    tofrom = df[(df['started_at'] > fromd) &
                (df['started_at'] < tod)]
    tofrom.to_csv('may23-june3.csv')


# Create the DAG and the tasks
with DAG('CleanData',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         # '0 * * * *',
         ) as dag:
    #    use PythonOperator and point it to your functions
    cleanData = PythonOperator(task_id='clean',
                               python_callable=cleanScooter)

    selectData = PythonOperator(task_id='filter',
                                python_callable=filterData)
    copyFile = BashOperator(task_id='copy',
                            bash_command='cp /home/xiaoyusun/may23-june3.csv /home/xiaoyusun/Desktop')
# specify the order of the tasks
    cleanData >> selectData >> copyFile
