
BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.ttmeiju-spider']
NEWSPIDER_MODULE = 'crawler.ttmeiju-spider'

ITEM_PIPELINES = {
    'crawler.ttmeiju-spider.ttmeiju-pipeline.TranslateNamePipeline': 300,
}