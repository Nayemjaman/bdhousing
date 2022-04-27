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

    def parse_details(self, response):
        title = (unicodedata.normalize("NFKD",response.css('h1 ::text').extract_first())).strip()
        location = (unicodedata.normalize("NFKD",response.css('h1 +p ::text').extract_first())).strip()
        price = (unicodedata.normalize("NFKD",response.css('.ct-productID ::text').extract_first())).strip()
        # PROPERTY SUMMARY
        heading = response.css('.detail-list label ::text').getall()
        heading = [i.strip() for i in heading]
        summary = response.css('.detail-list span ::text').getall()
        summary = [i.strip() for i in summary]
        
        #PROPERTY FEATURES
        features = response.css('.col-xs-6 label ::text').getall()
        features = [i.strip() for i in features]
        # Property Owner Details
        companey_name = response.css('h5 a ::text').get()
        property_id = response.css('h5 +p ::text').get()
        property_id = property_id.split(':')[1].strip()
        print(price)