from pymongo.database import Database
from pymongo import MongoClient


def get_db(db_name: str):
    client = MongoClient("localhost", 27017)
    return client[db_name]
