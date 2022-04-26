import scrapy


class BdhousingSpider(scrapy.Spider):
    name = 'bdhousing'
    allowed_domains = ['www.bdhousing.com']
    start_urls = ['http://www.bdhousing.com/']

    def parse(self, response):
        pass
