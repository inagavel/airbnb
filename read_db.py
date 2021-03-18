import pymongo as mongo
client = mongo.MongoClient()
db = client["airbnb"]
apart_collection = db['apart']

i = 0
for x in apart_collection.find({},{ "price"}):
  print(x["price"])
  i+=1
  if i == 5 :
      break

