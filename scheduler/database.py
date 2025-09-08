import os

from pymongo import MongoClient


def get_router_info():
    mongo_uri = os.environ.get("MONGO_URI")
    db_name = os.environ.get("DB_NAME")
    if not mongo_uri or not db_name:
        raise RuntimeError("MONGO_URI and DB_NAME must be set")

    client = MongoClient(mongo_uri)
    db = client[db_name]
    routers = db["routers"]

    # Return a materialized list of routers
    return list(routers.find())


if __name__ == "__main__":
    print(get_router_info())
