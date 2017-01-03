import scrapy

class chengItem(scrapy.Item):
    name = scrapy.Field()
    chinese_name = scrapy.Field()
    english_name = scrapy.Field()
    tags = scrapy.Field()
    size = scrapy.Field()
    siteid = scrapy.Field()
