import json
import pandas.io.json as pd_JSON

with open("data.JSON","r") as f:
# Use JSON.load() and pass the file reference to the method:
    data=json.load(f)
# Inspect the json by looking at the first record using the following:
    data['records'][0]
# Or just use the name:
    print(data['records'][0]['name'])

f=open('data.JSON','r')
data=pd_JSON.loads(f.read())

df=pd_JSON.json_normalize(data,record_path='records')
print(df.head(2).to_json())