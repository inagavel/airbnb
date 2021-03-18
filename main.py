
import pymongo as mongo
client = mongo.MongoClient()
db = client["bigdata"]
db.list_collection_names();
user_collection = db['user']
data = {'name': "Lufundisu", 'gender' : 'M', 'age' : 2}
print(user_collection.insert(data))

print(client.list_database_names())

for x in user_collection.find({},{ "age": 1.0}):
  print(x)

for x in user_collection.find({},{ "age": 1.0}):
  print(x)



