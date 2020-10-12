import logging

from pymongo import MongoClient

from api.config import settings

logger = logging.getLogger(__name__)

"""
MONGO_USER = "minerva"
MONGO_PASSWORD = os.getenv(
    "MINERVA_MONGO_PASSWORD"
)  # this environment variable will be set on the cloud
"""

def get_mongo_client():
    kwargs = {
        "connect": False,
        "connectTimeoutMs": 5000,
        "socketTimeoutMS": 30000,
        "serverSelectionTimeoutMS": 5000,
        #"username": "minerva",
        #"password": "password",
    }

    #uri = "mongodb://mongodb:27017/"

    try:
        client = MongoClient(settings.get("MONGO_URI") , **kwargs)
        #client.server_info()
    except Exception as e:
        logger.error('Unhandled error connecting to MongoDB: "{}"'.format(str(e)))
        raise

    return client


def get_mongo_collection(collection):
    client = get_mongo_client()
    db = client["minerva"]
    collection = db[collection]
    return collection


