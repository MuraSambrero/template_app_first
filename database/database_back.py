from pymongo.mongo_client import MongoClient
import os
from dotenv import main

main.load_dotenv()

mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')

uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@murasambrero.47hcogs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)