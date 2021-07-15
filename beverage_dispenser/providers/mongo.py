import os
from pymongo import MongoClient
from beverage_dispenser.constants import env

os.path.join(os.getcwd(), "beverage_dispenser")


# MongoDB Singleton
class MongoDB:
    __client = None
    __database = ''

    def __init__(self, database=env.MONGO_DATABASE):
        MongoDB.initialize(database)

    # Making sure only one connection is opened
    @staticmethod
    def initialize(database):
        MongoDB.__database = database
        if MongoDB.__client:
            return

        MongoDB.__client = MongoClient(
            f'mongodb://{env.MONGO_USERNAME}:{env.MONGO_PASSWORD}@' +
            f'{env.MONGO_HOST}:{env.MONGO_PORT}/{database}?authSource=admin'
        )

    @staticmethod
    def getClient():
        MongoDB.initialize(MongoDB.__database)
        return MongoDB.__client[MongoDB.__database]
