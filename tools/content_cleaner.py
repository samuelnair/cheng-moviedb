import pymongo


def connect_db():
    password = urllib.quote_plus('1qaz@WSX')
    uri = "mongodb://chenguser:" + password + "@127.0.0.1/chengdb?authMechanism=SCRAM-SHA-1"
    client = MongoClient(uri)
    db = client.chengdb

def find_unique():
