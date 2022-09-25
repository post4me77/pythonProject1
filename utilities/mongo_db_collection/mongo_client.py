from pymongo import MongoClient
from bson import ObjectId


class BaseMongoClient:
    def __init__(self, mongo_url, db_name):
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]

    def insert(self, data: list):
        self.db.insert_many(data)

    def delete_one(self, object_id):
        self.db.delete_one({"_id": ObjectId(str(object_id))})

    def delete_many(self, dict_of_objects):
        self.db.delete_many({dict_of_objects})

    def find_one(self, db_property, value):
        return self.db.find_one({db_property: value})

    def update(self, object_id, db_property, new_value):
        self.db.update({'_id': ObjectId(str(object_id))}, {'$set': {db_property: new_value}})
