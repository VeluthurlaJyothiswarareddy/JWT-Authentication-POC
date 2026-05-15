from pymongo import MongoClient
from config import settings

client = MongoClient(settings.mongo_uri)
db = client.jwt_poc
users_collection = db.users