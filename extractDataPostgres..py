import psycopg2 as db
import pandas as pd
from json import loads, dumps
conn_string="dbname='postgres' host='localhost' user='postgres' password='postgres'"
conn=db.connect(conn_string)
df=pd.read_sql("select * from users", conn)
df.to_json("pd.json")
# result=df.to_json(orient='records')
# parsed = loads(result)
# dumps(parsed, indent=4)  
