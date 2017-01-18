from pymongo import MongoClient
import urllib

password = urllib.quote_plus('1qaz@WSX')
uri = "mongodb://chenguser:" + password + "@127.0.0.1/chengdb?authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)
localdb = client.chengdb

uri2 = "mongodb://chenguser:" + password + "@120.77.205.216/chengdb?authMechanism=SCRAM-SHA-1"
server = MongoClient(uri2)
remotedb = server.chengdb

for doc in localdb.cleancontent.find():
    remotedoc = remotedb.cleancontent.find_one({"_id": doc["_id"]})
    print(remotedoc["chinese_name"])
