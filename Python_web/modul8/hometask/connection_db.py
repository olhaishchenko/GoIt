import configparser
from pymongo import MongoClient


config = configparser.ConfigParser()

config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'password')
mongo_db_name = config.get('DB', 'db_name')
mongo_domain = config.get('DB', 'domain')
# mongodb+srv://userweb9:567234@cluster0.byupvtg.mongodb.net/hometask
connection_string = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_domain}/{mongo_db_name}?retryWrites=true&w=majority"
client = MongoClient(connection_string)