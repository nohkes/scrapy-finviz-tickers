# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TickerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Stock(scrapy.Item):
    n = scrapy.Field()
    ticker = scrapy.Field()