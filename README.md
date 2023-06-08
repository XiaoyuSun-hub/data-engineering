# data-engineering

This project included sample code when I learning related technology about Data Engineering.
## Airflow
####  Building a CSV to a JSON  
Using a Bash and Python operator in Airflow build data pipeline(csvtojson.py).

####  Extract data from PostgreSQL, save it as a CSV file, read and write it to  Elasticsearch index
Using  two Python operators in Airflow build data pipeline (queryInsertDag.py).

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



#### cluster
download the packages and unzip the package and rename the shell script name(it is not neccessary step).
```
cp start-master.sh start-head.sh
cp start-slave.sh start-node.sh
```

build cluster by following command, the LAPTOP-7D78FTBR is the domain name for my VM
```
./spark3.2/sbin/start-head.sh
./spark-node3.2/sbin/start-node.sh spark://LAPTOP-7D78FTBR.localdomain:7077 -p 9911
```
visit http://localhost:8080/  you could see the node and tasks  
![Cluster](https://github.com/XiaoyuSun-hub/data-engineering/blob/master/pic/spark_cluster.png)

### Process data with PySpark
read,modify,filter,select data
code in processDataSpark.ipynb









