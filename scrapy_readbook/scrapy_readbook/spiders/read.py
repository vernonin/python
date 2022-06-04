import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1158_1.html']

    # follow=True 是否跟进，就是按照提取的链接规则一直进行提取

    rules = (
        Rule(LinkExtractor(allow=r'/book/1158_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@alt').extract_first()

            cover = img.xpath('./@data-original').extract_first()

            book = ScrapyReadbookItem(name=name, cover=cover)

            yield book
