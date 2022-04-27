import scrapy
import unicodedata


class BdhousingSpider(scrapy.Spider):
    name = 'bdhousing'
    allowed_domains = ['bdhousing.com']
    start_urls = ['https://www.bdhousing.com/features']

    def parse(self, response):
        housing_links = response.css('.ct-main-text .link_overlay::attr(href)').extract()
        housing_links = ['https://www.bdhousing.com'+i for i in housing_links]
        yield from response.follow_all(housing_links[:2], self.parse_details)

    
