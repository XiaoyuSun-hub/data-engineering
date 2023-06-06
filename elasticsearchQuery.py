# from elasticsearch import helpers
from elasticsearch import Elasticsearch
from pandas import json_normalize
from faker import Faker
fake=Faker()
es = Elasticsearch()
es=Elasticsearch({'127.0.0.1'})

# doc={"query":{"match_all":{}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'])
# for doc in res['hits']['hits']:
#  print(doc['_source'])

# df=json_normalize(res['hits']['hits'])
# print(df)

# doc={"query":{"match":{"name":"Ronald Goodman"}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'][0]['_source'])

# res=es.search(index="users",q="name:Ronald Goodman",size=10)
# print(res['hits']['hits'][0]['_source'])

# Get City Jamesberg - Returns Jamesberg and Lake Jamesberg
# doc={"query":{"match":{"city":"Lake Logan"}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'])

# Get Jamesberg and filter on zip so Lake Jamesberg is removed
# doc={"query":{"bool":{"must":{"match":{"city":"Lake Logan"}},
# "filter":{"term":{"zip":"80891"}}}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'])
# https://www.elastic.co/guide/en/elasticsearch/reference/current/api-conventions.html#time-units
res = es.search(
 index = 'users',
 doc_type = 'doc',
 scroll = '20s',
 size = 5,
#  body = {"query":{"match_all":{}}}
 body = {"query":{"match":{"city":"Lake Logan"}}}
 
)

#  doc={"query":{"match":{"name":"Ronald Goodman"}}}
sid = res['_scroll_id']
size = res['hits']['total']['value']
print(size)

while (size > 0):
    res = es.scroll(scroll_id = sid, scroll = '2ms')
    sid = res['_scroll_id']
    size = len(res['hits']['hits'])
    for doc in res['hits']['hits']:
        print(doc['_source'])






