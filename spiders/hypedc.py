# -*- coding: utf-8 -*-
import scrapy

from scrap_hypedc.items import ScrapHypedcItem


class HypedcSpider(scrapy.Spider):
    name = "hypedc"
    allowed_domains = ["hypedc.com"]
    start_urls = [
        'https://www.hypedc.com/mens/footwear/sneakers/'
        ]
    
    def parse(self, response):
        product_urls = response.xpath('//div[@class="item col-xs-12 col-sm-6"]/a/@href').extract()
    
        for url in product_urls:
            yield scrapy.Request(url, callback=self.parse_summary)
        pass
    def parse_summary(self, response):
        item = ScrapHypedcItem()
        gender = 'Men'
        name = response.xpath('//h1[@class="product-name"]/text()').extract()
        info = response.xpath('//meta/@content').extract()
        color = response.xpath('//h3[@class="h4 product-colour"]/text()').extract()
        
        item['product_url'] = ''.join(info[14]).strip()
        item['gender'] = ''.join(gender).strip()
        item['product_name'] = ''.join(name).strip()
        item['product_price'] = ''.join(info[18]).strip()
        item['product_color'] = ','.join(color).strip()
        item['currency'] = ''.join(info[19]).strip()
        yield item

    
