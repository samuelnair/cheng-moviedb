import requests
import urllib
import time
from pymongo import MongoClient

password = urllib.quote_plus('1qaz@WSX')
uri = "mongodb://chenguser:" + password + "@127.0.0.1/chengdb?authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)
db = client.chengdb


for content in db.cleancontent.find():
    payload = {"q": content["_id"]}
    r = requests.get("http://api.douban.com/v2/movie/search", params=payload)
    print(r.url)
    data = r.json()
    #print data['subjects'][0]['images']
    if data["subjects"]:
        image_rec = {
            "_id": content["_id"],
            "small": data['subjects'][0]['images']['small'],
            "medium": data['subjects'][0]['images']['medium'],
            "large": data['subjects'][0]['images']['large']
        }
        db.contentimages.insert_one(image_rec)
    time.sleep(20)
