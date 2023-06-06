import pandas as pd
# df=pd.read_csv('data.CSV')
# df.head(10)
data={'Name':['Paul','Bob','Susan','Yolanda'],
'Age':[23,45,18,21]}
df2=pd.DataFrame(data)
df2.to_csv('fromdf.CSV',index=False)