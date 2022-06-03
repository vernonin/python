import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem


class DangSpider(scrapy.Spider):
    name = 'dang'
    # allowed_domains 请求域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.03.42.00.00.00.html']

    base_url = "http://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        li_list = response.xpath('//*[@id="component_59"]/li')

        for li in li_list:
            cover = li.xpath('.//img/@data-original').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            
            # 第一张图片没有data-original属性
            if cover:
                cover = cover
            else:
                cover = li.xpath('.//img/@src').extract_first()

            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            detail = li.xpath('.//p[@class="detail"]/text()').extract_first()
            
            book = ScrapyDangdangItem(cover=cover, name=name, price=price, detail=detail)

            # 获取一个book就把book交给popelines管道
            yield book


        if self.page < 100:
            self.page = self.page + 1

            url = self.base_url + str(self.page) + "-cp01.03.42.00.00.00.html"
            
            # scrapy.Request()就是scrapy就get请求
            # url 就是请求地址
            # callback 就是你要执行的函数 注意不需要加：()
            yield scrapy.Request(url=url, callback=self.parse)