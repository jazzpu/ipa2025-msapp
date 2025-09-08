from pymongo import MongoClient
from datetime import datetime, UTC
import os


def save_interface_status(router_ip, interfaces):
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["interfaces_status"]

    data = {
        "router_ip": router_ip,
        "interfaces": interfaces,
        "timestamp": datetime.now(UTC)
    }

    collection.insert_one(data)
    print(f"Saved interface status for router {router_ip} to MongoDB")
    client.close()
