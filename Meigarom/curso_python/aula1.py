
import pandas as pd

data = pd.read_csv('archive/kc_house_data.csv')

print(data.head())

print(data.shape)

print(data.columns)

print(data[['id','price']])

print(data[['id','price']].sort_values('price', ascending=False))