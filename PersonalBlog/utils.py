from pymongo import MongoClient
from django.conf import settings

def get_db_handle():
    client = MongoClient(settings.MONGO_URI)
    db_handle = client.get_default_database()
    return db_handle, client
