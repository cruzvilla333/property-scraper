import scrapy
import re
import csv
from realtor_scraper.items import PropertyItem 

def getPageNumber(url):
            result = ''
            i = len(url) - 1
            while url[i].isdigit():
                result += url[i]
                i -= 1
            return result[::-1]
        
start_url1 = 'https://www.realtor.com/realestateandhomes-search/Lehigh-Acres_FL/type-land/lot-sqft-10890-13068'

class RealtorscraperSpider(scrapy.Spider):
    
    
    name = "realtorscraper"
    allowed_domains = ["www.realtor.com"]
    start_urls = [start_url1]

    average_price = 0

    def parse(self, response):
        
        properties = response.css('.BasePropertyCard_propertyCardWrap__J0xUj')
            
        for property in properties:
            property_item = PropertyItem()
            property_item['price'] = property.css('.card-price::text').get()
            property_item['size'] = f'{property.css(".meta-value::text").get()}'
            property_item['address'] = property.css('.truncate-line::text').get()

            yield property_item
        next_url = response.css('.next-link::attr(href)').get()
        if(next_url): 
            yield response.follow(f'{start_url1}/pg-{getPageNumber(next_url)}', callback = self.parse)
                
    
    
    