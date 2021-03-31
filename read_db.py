from airbnb_mysql import *
import csv
import pandas as pd


port_name = '3306'
user_name = 'root'
user_password = 'root'
host_name = 'localhost'
db = 'airbnb'


connection = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)

query = """
        SELECT * FROM apartment;
"""
db_read = read_query(connection,query)
from_db = []
for val in db_read:
    from_db.append(val)

col_name = ["id","neighbour","lat","long","r_type","price","nbr_rev","rev_per_month"]
df = db_to_df(connection,query,col_name)

print(df)