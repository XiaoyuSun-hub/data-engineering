# data-engineering

This project included sample code when I learning related technology about Data Engineering.
## Airflow
####  Building a CSV to a JSON  
Using a Bash and Python operator in Airflow build data pipeline(csvtojson.py).

(pic)

####  Extract data from PostgreSQL, save it as a CSV file, read and write it to  Elasticsearch index
Using  two Python operators in Airflow build data pipeline (queryInsertDag.py).

(pic)

#### Cleaning,filter,write it

Using a Bash and two Python operators in Airflow build data pipeline (cleandataAirflow.py).

![cleandataAirflow](https://github.com/XiaoyuSun-hub/data-engineering/blob/master/pic/airflow_cleandata.jpg)


## NoSQL database(Elasticsearch) 
#### Insert data using The index or helper method .
(elasticsearchInsert.py)  
Verify the results Kibana.

![Kibana](https://github.com/XiaoyuSun-hub/data-engineering/blob/master/pic/elastic_kibanna.png)


#### Extract data using search, combine with scroll for large results.
 (elasticsearchQuery.py)
 
##  Spark
### why Spark?
support both streams and batch data  
fast   
distribute processing tasks across multiple computers through cluster  

### Process data with PySpark
read,modify,filter,select data
code in processDataSpark.ipynb

![Cluster](https://github.com/XiaoyuSun-hub/data-engineering/blob/master/pic/spark_cluster.png)







