from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime

# load .env file
load_dotenv()

# get connection string from env
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["startup_ai"]
collection = db["chat_history"]

def init_db():
    pass

def save_message(role, content):
    collection.insert_one({
        "role": role,
        "content": content,
        "timestamp": datetime.datetime.utcnow()
    })

def load_history():
    messages = collection.find().sort("timestamp", 1)
    return [
        {"role": m["role"], "content": m["content"]}
        for m in messages
    ]

def clear_history():
    collection.delete_many({})