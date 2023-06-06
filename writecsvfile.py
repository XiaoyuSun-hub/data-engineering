from faker import Faker
import csv
# output=open('data.CSV','w')
with open('data.CSV', 'w') as data_file:
    output = data_file
    fake=Faker()
    header=['name','age','street','city','state','zip','lng','lat']
    mywriter=csv.writer(output)
    mywriter.writerow(header)
    for r in range(1000):
        mywriter.writerow([fake.name(),fake.random_int(min=18, max=80, step=1), fake.street_address(), fake.city(),
                    fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
    output.close()