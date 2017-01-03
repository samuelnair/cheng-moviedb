
import scrapy
from scrapy.loader import ItemLoader
from crawler.dataitem import chengItem

class TTMeijuSpider(scrapy.Spider):
    name = 'ttmeiju-spider'
    start_urls = ['http://www.ttmeiju.com/meiju/Movie.html']

    def parse(self, response):
        for seedlist in response.xpath('//tr[@class="Scontent"]'):
            l = ItemLoader(item=chengItem(), selector=seedlist)
            l.add_xpath('name', './/td[3]/a/text()')
            l.add_xpath('size','.//td[6]/text()')
            l.add_xpath('siteid','.//td[0]/input/@value')
            yield l.load_item()
        next_page_url = response.xpath('//a[@class="next"]//@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
