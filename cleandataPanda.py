import pandas as pd
df = pd.read_csv('scooter.csv')
# drop column inplace is ture will modify orginal data
# df.drop(columns=['region_id'], inplace=True)

# # drop row with index
# df.drop(index=[34225], inplace=True)
# df['start_location_name'][(df['start_location_name'].isnull())]
# df.dropna(subset=['start_location_name'], inplace=True)
# fill null with zero
# df.fillna(value='00:00:00', axis='columns')

# #  copy the rows where both the start and end location are nul
# startstop = df[(df['start_location_name'].isnull())
#                & (df['end_location_name'].isnull())]
# value = {'start_location_name': 'Start St.', 'end_location_name': 'Stop St.'}
# startstop.fillna(value=value)
# startstop[['start_location_name', 'end_location_name']]
# # drop row with month may
# may = df[(df['month'] == 'May')]
# df.drop(index=may.index, inplace=True)

# create and modify
# df.columns = [x.lower() for x in df.columns]
# print(df.columns)
# df.rename(columns={'DURATION': 'duration',
#           'region_id': 'region'}, inplace=True)
# df['month'] = df['month'].str.upper()
# df['month'].head()
# # create column
# df['month'] = df['month'].str.upper()
# df['month'].head()
# splitting the data and then inserting it into the DataFrame
# d = pd.DataFrame()
# d.columns
# df[['trip_id', 'started_at']].head()
# df['started_at'].str.split()
# print(df)
# new = df['started_at'].str.split(expand=True)
# df['date'] = new[0]
# df['time'] = new[1]
# print(df)


# df['started_at2'] = pd.to_datetime(
#     df["started_at"]).dt.strftime("%Y-%m-%d %H:%M")
# df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
# print(df.dtypes)
# when = '2019-07-10'
# x = df[(df['started_at'] > when)]
# print(x)

# enriching data
new = pd.DataFrame(df['start_location_name'].value_counts().
                   head())
new.reset_index(inplace=True)
new.columns = ['address', 'count']
print(new)

n = new['address'].str.split(pat=',', n=1, expand=True)
replaced = n[0].str.replace("@", "and")
new['street1'] = n[0]
new['street'] = replaced
print(new)

geo = pd.read_csv('geocodedstreet.csv')
joined = new.join(other=geo, how='left', lsuffix='_new', rsuffix='_geo')
print(joined[['street_new', 'street_geo', 'x', 'y']])
merged = pd.merge(new, geo, on='street')
print(merged.columns)
print(merged)
