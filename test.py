import psycopg2 as db 
import pandas as pd

conn_string="dbname='postgres' host='localhost' user='postgres' password='postgres'"
conn=db.connect(conn_string)
df=pd.read_sql("select name,city from users",conn)
df.to_csv('postgresqldata.csv')
print("-------Data Saved------")