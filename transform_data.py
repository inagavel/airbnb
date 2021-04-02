from airbnb_mysql import *
import seaborn as sns
import csv
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import KBinsDiscretizer
import matplotlib.pyplot as plt
import numpy as np

port_name = '3306'
user_name = 'root'
user_password = 'root'
host_name = 'localhost'
db = 'airbnb'

connection = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)

query = """
        SELECT * FROM apartment;
"""

col_name = ["id", "neighbour", "lat", "long", "r_type", "price", "nbr_rev", "rev_per_month"]
df = db_to_df(connection, query, col_name)

new_df = df.drop(['id', 'nbr_rev', 'rev_per_month'], axis=1)
new_df = new_df[df != 0].dropna()
#new_df = new_df[df['price'] < 500].dropna()
print(new_df.describe())

for col in new_df.select_dtypes('object'):
    print(f'{col:-<50} {new_df[col].unique()}')

#neighbour
encoder = LabelEncoder()
neigh = encoder.fit_transform(new_df["neighbour"])
new_df['nbh'] = neigh

#room
room_encoder = LabelEncoder()
room = room_encoder.fit_transform(new_df["r_type"])
new_df["room"] = room

new_df.sort_values('room', axis=0, inplace=True)
new_df = new_df.reset_index(drop=True)

print(new_df)
print(new_df['r_type'].value_counts())

grouped_df = new_df.groupby(['r_type'])
print(grouped_df['price'].mean())

print(new_df['neighbour'].value_counts())

grouped_df = new_df.groupby(['neighbour'])
print(grouped_df['price'].mean())

sns.boxplot(x='r_type',y='price',data=new_df)
plt.show()
"""
price = new_df['price']
row_list = list(new_df.index.values)
room = new_df["room"]

plt.figure()
plt.scatter(row_list, price, c=room)
plt.show()
"""
