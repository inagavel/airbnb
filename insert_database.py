import pymongo as mongo
import csv
import pandas as pd

import json
client = mongo.MongoClient()
db = client["airbnb"]
apart_collection = db['apart']

with open('list.csv', 'r', encoding='Latin1') as csv_file:
    csv_reader = csv.reader(csv_file)
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
