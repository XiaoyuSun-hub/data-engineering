from elasticsearch import Elasticsearch
from faker import Faker
fake=Faker()
from elasticsearch import helpers


# from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200/")
# es.info().body
# doc={"name": fake.name(),"street": fake.street_address(), 
# "city": fake.city(),"zip":fake.zipcode()}
# res=es.index(index="users",doc_type="doc",body=doc)
# print(res['result']) #created

actions = [
 {
    "_index": "users",
    "_type": "doc",
    "_source": {
    "name": fake.name(),
    "street": fake.street_address(), 
    "city": fake.city(),
    "zip":fake.zipcode()}
 }
 for x in range(998) # or for i,r in df.iterrows()
]
res = helpers.bulk(es, actions)
print(res[0])
