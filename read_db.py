from airbnb_mysql import *
import csv
import pandas as pd

port_name = '3306'
user_name = 'root'
user_password = 'root'
host_name = 'localhost'
db = 'airbnb'

connection = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)

with open('list.csv', 'r', encoding='Latin1') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_app = []
    for line in csv_reader:
        app_id = line[0]
        reviews_per_month = line[13]
        apartment = (app_id, reviews_per_month)
        list_app.append(apartment)

for app in list_app:
    query = """
            UPDATE apartment
            SET review_per_month = {}
            WHERE id ={}; 
            """.format(app[0], app[1])
    execute_query(connection, query)
connection.close()
