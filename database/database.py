from pymongo import MongoClient
from fake_db import fake_db

client = MongoClient('mongodb://localhost:27017/')

def append_template_in_mongodb(client, *args, **kwargs):  # для добавления fake_db в MongoDB
    db = client['templates_db']
    collection = db['templates']
    template = dict(*args, **kwargs)
    collection.insert_one(template)

for elem in fake_db: # Для добавления fake_db в бд MongoDB
    append_template_in_mongodb(client, elem)