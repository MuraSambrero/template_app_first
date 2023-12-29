import os

class Config:
    database_url = os.environ.get('MONGO_DATABASE_URL')
    mongo_pass = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    mongo_user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    mongo_port = os.environ.get('MONGO_PORT')
    uri = f"mongodb://{mongo_user}:{mongo_pass}@{database_url}:{mongo_port}/"
    mongo_init_db_name = os.environ.get('MONGO_INITDB_DATABASE')
    collection_name = 'templates'
