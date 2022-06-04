# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDianyingtiantangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 封面
    cover = scrapy.Field()

