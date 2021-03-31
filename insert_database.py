from airbnb_mysql import *
import csv
import pandas as pd
import json

with open('list.csv', 'r', encoding='Latin1') as csv_file:
    csv_reader = csv.reader(csv_file)
    '''
    for line in csv_reader:
        print(
            f"id :{line[0]} ngb: {line[5]} lat: {line[6]} long: {line[7]} type: {line[8]} price: {line[9]} rev: {line[11]} rpm:  {line[13]}")

 
    next(csv_reader)
    for line in csv_reader:
        data = {
            "id": line[0],
            "neighbourhood": line[5],
            "latitude": line[6],
            "longitude": line[7],
            "room_type": line[8],
            "price": line[9],
            "number_of_reviews": line[11],
            "reviews_per_month": line[13]
        }
        apart_collection.insert_one(data)
    '''
    list_app = []
    for line in csv_reader:
        app_id = line[0]
        neighbourhood = line[5]
        latitude = line[6]
        longitude = line[7]
        room_type = line[8]
        price = line[9]
        number_of_reviews = line[11]
        reviews_per_month = '0'
        apartment = (app_id, neighbourhood, latitude, longitude, room_type, price, number_of_reviews, reviews_per_month)
        list_app.append(apartment)


query1 = 'CREATE DATABASE IF NOT EXISTS airbnb;'

query = """
        CREATE TABLE IF NOT EXISTS apartment (
        id INTEGER AUTO_INCREMENT,
        neighbourhood VARCHAR(255),
        latitude DOUBLE,
        longitude DOUBLE,
        room_type   VARCHAR(255),
        price      DOUBLE,
        number_of_reviews    INTEGER,
        reviews_per_month    DOUBLE,
        PRIMARY KEY (id)
         );
        """

port_name = '3306'
user_name = 'root'
user_password = 'root'
host_name = 'localhost'

drop_table = 'DROP TABLE apartment'
cnx = create_server_connection(user=user_name, password=user_name, host=host_name, port=port_name)
execute_query(cnx, query1)
db = 'airbnb'
cnx = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)

# execute_query(cnx, drop_table)
execute_query(cnx, query)
cnx.close()

cnx = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)
for app in list_app:
    print(app)
    insert_query = '''
    INSERT INTO apartment VALUES
    {}
    '''.format(app)
    execute_query(cnx, insert_query)

cnx.close
