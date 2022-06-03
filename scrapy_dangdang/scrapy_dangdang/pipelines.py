# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话，那么就必须在settings中开启管道
class ScrapyDangdangPipeline:
    # 在爬虫文件开始之前就执行
    def open_spider(self, spider):
        self.fp = open("books.json", "w", encoding="utf-8")



    # item就是yield后面的book字典
    def process_item(self, item, spider):
        
        # with open("book.json", "a", encoding="utf-8") as f:
        #     # 1. write方法必须要写一个字符串，而不能是其他类型
        #     # 2. w模式，会每个对象都打开一次文件，并覆盖之前的内容
        #     f.write(str(item) + ",")

        self.fp.write(str(item) + ",")

        return item

    
    # 在爬虫文件执行完之后执行
    def close_spider(self, spider):
        self.fp.close()


# 开启多条管道
'''
    1. 定义管道类
    2. 在settings中开启管道
'''
class DangDangDownloadPipeline:
    def process_item(self, item, spider):

        url = "http:" + item.get("cover")
        filenaem = "./books/" + item.get("name") + ".jpg"

        urllib.request.urlretrieve(url=url, filename=filenaem)

        return item