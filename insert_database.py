from airbnb_mysql import *
import pymongo as mongo
import csv
import pandas as pd

import json
client = mongo.MongoClient()
db = client["airbnb"]
apart_collection = db['apart']

with open('list.csv', 'r', encoding='Latin1') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(f"id :{line[0]} ngb: {line[5]} lat: {line[6]} long: {line[7]} type: {line[8]} price: {line[9]} rev: {line[11]} rpm:  {line[13]}")

    '''
    next(csv_reader)
    for line in csv_reader:
        data = {
            "id": line[0],
            "neighboourhood": line[5],
            "latitude": line[6],
            "longetude": line[7],
            "room_type": line[8],
            "price": line[9],
            "number_of_reviews": line[11],
            "reviews_per_month": line[13]
        }
        apart_collection.insert_one(data)
    '''

query1 = 'CREATE DATABASE IF NOT EXISTS airbnb;'

query = 'CREATE TABLE IF NOT EXISTS apartment'
query += ' ('
query += '        id INTEGER AUTO_INCREMENT,'
query += '        neighboourhood VARCHAR(255),'
query += '        latitude DOUBLE,'
query += '        longetude DOUBLE,'
query += '        room_type   VARCHAR(255),'
query += '        price      DOUBLE,'
query += '        number_of_reviews    INTEGER,'
query += '        reviews_per_month    DOUBLE,'
query += '        PRIMARY KEY (id))'

port_name = '3306'
user_name = 'root'
user_password = 'root'
host_name = 'localhost'

cnx = create_server_connection(user=user_name, password=user_name, host=host_name, port=port_name)
execute_query(cnx, query1)
db = 'airbnb'
cnx = create_db_connection(user=user_name, password=user_name, host=host_name, db_name=db, port=port_name)
execute_query(cnx, query)
cnx.close()