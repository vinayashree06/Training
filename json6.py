#indexing a series using iloc
import pandas as pd
df=pd.read_csv('data.csv')
ser=pd.Series(df['name'])
data=ser.head(5)
print(data)