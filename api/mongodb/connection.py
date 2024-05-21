import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from api.mongodb.models.RequestModel import User

load_dotenv()
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.fojdvk6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
db = client.get_database("requests")
collection = db.get_collection("requests")


def select_from_mongo():
    try:
        session = client.start_session()
        data = collection.find_one({"user": "mrstreamer"})
        return data

    except Exception as e:
        print(e)

    finally:
        session.end_session()


select_from_mongo()
