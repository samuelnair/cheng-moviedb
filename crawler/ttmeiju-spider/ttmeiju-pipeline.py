from scrapy.exceptions import DropItem
from pymongo import MongoClient
import urllib
import re

class TranslateNamePipeline(object):

    def open_spider(self,spider):
        # self.file = open('items.jl', 'wb')
        password = urllib.quote_plus('1qaz@WSX')
        uri = "mongodb://chenguser:"+password+"@127.0.0.1/chengdb?authMechanism=SCRAM-SHA-1:27017"
        client = MongoClient(uri)
        self.db = client.chengdb

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        if item['name']:
            # Need to extract the Chinese and the English name
            # Most of the titles are in this format
            # <ChineseName> <EnglighName> <year> <rez(720p|1080p)> <source(WebRip,Bluray...)> <ChineseGroup> <FileType>
            m = re.search('(.*?)\s(.*?)\s([1-2][9,0][0-9][0-9])\s(.*?)$',item['name'][0])
            if m:
                item['chinese_name'] = m.group(1)
                item['english_name'] = m.group(2)
                item['tags'] = [m.group(3)] + m.group(4).split()
            self.db.content.insert_one(dict(item))
            # line = json.dumps(dict(item)) + "\n"
            # self.file.write(line)
            return item
        else:
            raise DropItem("Missing Name" % item)
