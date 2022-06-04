import scrapy
from scrapy_dianyingtiantang.items import ScrapyDianyingtiantangItem

class MoveSpider(scrapy.Spider):
    name = 'move'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字和第二页的封面图
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            
            # 第二页的链接
            url = 'https://www.ygdy8.net/' + href

            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    



    def parse_second(self, response):
        # 接收到请求的meta参数的值
        name = response.meta['name']

        # 如果拿不到数据的情况下，要检查xpath语法是否正确
        cover = response.xpath('//*[@id="Zoom"]//img/@src').extract_first()

        movie = ScrapyDianyingtiantangItem(cover=cover, name=name)

        yield movie
