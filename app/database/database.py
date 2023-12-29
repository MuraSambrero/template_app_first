from pymongo import MongoClient
from config import Config

print(Config.uri)
client = MongoClient(Config.uri)

def append_template_in_mongodb(client, *args, **kwargs):  # для добавления fake_db в MongoDB
    db = client[Config.mongo_init_db_name]
    collection = db[Config.collection_name]
    template = dict(*args, **kwargs)
    collection.insert_one(template)
