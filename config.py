import os
from dotenv import main

main.load_dotenv()

class Config:
    database_url = os.getenv('MONGO_DATABASE_URL')
    mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    mongo_port = os.getenv('MONGO_PORT')
    uri = f"mongodb://{mongo_user}:{mongo_pass}@{database_url}:{mongo_port}/"
    mongo_init_db_name = os.getenv('MONGO_INITDB_DATABASE')
    collection_name = 'templates'