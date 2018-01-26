import pprint
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
db = client.roomNo301
collection = db.roommates
# collection.insert({"name": "v",
#      "age": "24",
#      "eyecolor" : "blue",
#      "weight" : "100",
#      "gender" : "male"})
pprint.pprint(collection.find_one())
pprint.pprint(collection.count())
pprint.pprint(collection.find_one({"eyecolor":"brown"}))
pprint.pprint(collection.find({"age":"23"}).count())

