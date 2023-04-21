import scrapy
import unicodedata
from ..items import BdhousingScraperItem


class BdhousingSpider(scrapy.Spider):

    name = 'bdhousing'
    allowed_domains = ['bdhousing.com']
    start_urls = ['https://www.bdhousing.com/features']

    def parse(self, response):
        housing_links = response.css(
            '.ct-main-text .link_overlay::attr(href)').extract()
        housing_links = ['https://www.bdhousing.com'+i for i in housing_links]
        yield from response.follow_all(housing_links[:2], self.parse_details)

    def parse_details(self, response):
        item = BdhousingScraperItem()

        
        title = (unicodedata.normalize("NFKD", response.css(
            'h1 ::text').get())).strip()
        location = (unicodedata.normalize("NFKD", response.css(
            'h1 +p ::text').get())).strip()
        price = (unicodedata.normalize("NFKD", response.css(
            '.ct-productID ::text').get())).strip()

        # Property summary
        heading = response.css('.detail-list label ::text').getall()
        heading = [unicodedata.normalize("NFKD", i) for i in heading]
        heading = [i.strip() for i in heading]
        summary = response.css('.detail-list span ::text').getall()
        summary = [i.strip() for i in summary]
        property_summary = dict(zip(heading, summary))

        # Property details
        features = response.css('.col-xs-6 label ::text').getall()
        features = [i.strip() for i in features]
        features = [i for i in features if len(i) > 0]
        features = ",".join(features)

        # Property Owner Details
        companey_name = response.css('h5 a ::text').get()
        property_id = response.css('h5 +p ::text').get()
        property_id = property_id.split(':')[1].strip()

        item['title'] = title
        item['location'] = location
        item['price'] = price

        item['property_summary'] = property_summary

        item['features'] = features
        item['companey_name'] = companey_name
        item['property_id'] = property_id
        yield item
