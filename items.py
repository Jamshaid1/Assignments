# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapHypedcItem(scrapy.Item):
    # define the fields for your item here like:
     product_url = scrapy.Field()
     gender = scrapy.Field()
     product_name = scrapy.Field()
     product_price = scrapy.Field()
     product_color = scrapy.Field()
     currency = scrapy.Field()
    
