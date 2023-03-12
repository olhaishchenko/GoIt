import configparser
from pymongo import MongoClient


config = configparser.ConfigParser()

config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'password')
mongo_db_name = config.get('DB', 'db_name')
mongo_domain = config.get('DB', 'domain')

connection_string = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_domain}/{mongo_db_name}?retryWrites=true&w=majority"
client = MongoClient(connection_string)