# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtorScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value):
    value = value.replace(',', '')
    value = value.replace('$', '')
    return value

class PropertyItem(scrapy.Item):
    price = scrapy.Field(serializer = serialize_price)
    size = scrapy.Field()
    address = scrapy.Field()
