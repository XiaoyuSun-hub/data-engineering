from faker import Faker
import json
output=open('data.JSON','w')
fake=Faker()
alldata={}
alldata['records']=[]
for x in range(300):
    data={"name":fake.name(),
          "age":fake.random_int(min=18, max=80, step=1),
            "street":fake.street_address(),
            "city":fake.city(),"state":fake.state(),
            "zip":fake.zipcode(),
             "lng":float(fake.longitude()),
             "lat":float(fake.latitude())}
    alldata['records'].append(data)
json.dump(alldata,output)
