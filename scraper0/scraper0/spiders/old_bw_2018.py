# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider

class LinkItem(scrapy.Item):
    link = scrapy.Field()

class OldBw2018Spider(scrapy.Spider):
    name = 'old_bw_2018'
    allowed_domains = ['iwf.net/']
    start_urls = ['http://www.iwf.net/results/results-by-events/?event_year=' + str(x) for x in range(1998,2019)]

    def parse(self, response):
        events = response.xpath('//td[2]/a/@href').extract() 
        for event in events:
            item = LinkItem()
            item['link'] = response.urljoin(event)
            yield item     


        
   