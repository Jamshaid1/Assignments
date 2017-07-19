# -*- coding: utf-8 -*-
import scrapy

from scrap_hypedc.items import ScrapHypedcItem


class HypedcSpider(scrapy.Spider):
    name = "hypedc"
    allowed_domains = ["hypedc.com"]
    start_urls = [
        'https://www.hypedc.com/brands/'
        ]
    
    def parse(self,response):
        brands_urls = response.xpath('//li[@class="tertiary-item"]/a/@href').extract()
    
        for url in brands_urls:
            yield scrapy.Request(url, callback=self.parse_brands)
        pass
    def parse_brands(self, response):
        product_urls = response.xpath('//div[@class="item col-xs-12 col-sm-6"]/a/@href').extract()
    
        for url in product_urls:
            yield scrapy.Request(url, callback=self.product_detail)
        pass
    def product_detail(self, response):
        item = ScrapHypedcItem()
        name = response.xpath('//h1[@class="product-name"]/text()').extract()
        info = response.xpath('//meta/@content').extract()
        color = response.xpath('//h3[@class="h4 product-colour"]/text()').extract()
        brand_name = response.xpath('//span[@class="brand-name"]/text()').extract()
        
        brand_detail = {"product_url": "","product_name": "", "product_color": "", "currency": "AUD", "product_price": ""}
        brand_detail['product_url'] = ''.join(info[14]).strip() # return product_url
        brand_detail['product_price'] = ''.join(info[18]).strip()# return product_price
        brand_detail['currency'] = ''.join(info[19]).strip() # return type of currency
        brand_detail['product_name'] = ''.join(name).strip()
        brand_detail['product_color'] = ','.join(color).strip()
        brand_detail['brand_name'] = ''.join(brand_name[0]).strip()
        
        item['brand'] = brand_detail
        
        yield item

    
