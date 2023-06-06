import pandas as pd
df = pd.read_csv('scooter.csv')
print(df.columns)
print(df.dtypes)
print(df.head(10))
# To display all the columns
pd.set_option('display.max_columns', 500)
df['DURATION']
df[['trip_id', 'DURATION', 'start_location_name']]
# pull sample
df.sample(5)
# first 10 row
df[:10]
# extract the specific row
df.loc[33]
# row and column
df.at[2, 'DURATION']
# DataFrames to select rows based on some condition
user = df.where(df['user_id'] == 8417864)  # df[(df['user_id']==8417864)]
# combine conditional statements.
one = df['user_id'] == 8417864
two = df['trip_ledger_id'] == 1488838
df.where(one & two)
df[(one) & (two)]
# five-number summary cound mean std min 25% 50% 75% max
df.describe()
df['start_location_name'].describe()
# get the value and count for all unique values
df['DURATION'].value_counts()
#  the frequency as a percentage, you can pass the normalize
df['DURATION'].value_counts(normalize=True)
# drop null
df['end_location_name'].value_counts(dropna=False)
#  how many missing values in column
df.isnull().sum()
