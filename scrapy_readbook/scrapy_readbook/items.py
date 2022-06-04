# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyReadbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    name = scrapy.Field()
    #封面
    cover = scrapy.Field()
