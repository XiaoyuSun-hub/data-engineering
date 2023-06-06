import psycopg2 as db
conn_string="dbname='postgres' host='localhost'user='postgres' password='postgres'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "select * from users"
cur.execute(query)
for record in cur:
 print(record)
cur.fetchall()
# cur.fetchmany(howmany) # where howmany equals the number of records you want returned 
# cur.fetchone() cur.rownumber
cur.rowcount
f=open('fromdb.csv','w')
cur.copy_to(f,'users',sep=',')
f.close()
f=open('fromdb.csv','r')
f.read()
