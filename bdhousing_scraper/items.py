# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BdhousingScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()

    property_summary = scrapy.Field()
    
    features = scrapy.Field()
    companey_name = scrapy.Field()
    property_id = scrapy.Field()

