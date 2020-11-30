from pymongo import MongoClient
import datetime

class MongoClientObject(object):
    def __init__(self, MongoURL, databaseName, collection):
        self.client = MongoClient(MongoURL)
        self.database = self.client[databaseName]
        self.collection = self.database[collection]

    def insert(self, dataEntry):
        self.collection.insert(dataEntry)
