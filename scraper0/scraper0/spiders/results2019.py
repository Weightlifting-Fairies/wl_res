# -*- coding: utf-8 -*-


#########################
#Old refer to new_bw_2019
#########################




import scrapy
from scrapy import Spider
from scrapy.http import Request

class LinkItem(scrapy.Item):
    link = scrapy.Field()

class Results2019Spider(Spider):
    name = 'results2019'
    allowed_domains = ['iwf.net/']
    start_urls = ['https://www.iwf.net/new_bw/results_by_events/?event_year=201%d/' %i for i in range(9, 7, -1)]

    def parse(self, response):
        events = response.xpath('//td[2]/a/@href').extract() 
        for event in events:
            item = LinkItem()
            item['link']= response.urljoin(event)
            yield item

        #process previous year
        #prev_year_url = response.xpath('//*[@id="prev_year"]/a/@href').extract_first()  
        #absolute_prev_year_url = response.urljoin(prev_year_url)
        #yield scrapy.Request(absolute_prev_year_url, callback=self.parse_event)


    def parse_event(self, response):
        pass
       

