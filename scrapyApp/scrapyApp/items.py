# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from spider.models import Item

class ScrapyappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SearchItem(DjangoItem):
    django_model = Item
    name = scrapy.Field()
    price = scrapy.Field()