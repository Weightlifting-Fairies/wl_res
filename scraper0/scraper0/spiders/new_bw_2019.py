# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Spider


class LinkItem(scrapy.Item):
    #link = scrapy.Field()
    download_link = scrapy.Field()

class NewBw2019Spider(scrapy.Spider):
    name = 'new_bw_2019'
    allowed_domains = ['iwf.net/']
    start_urls = ['https://www.iwf.net/new_bw/results_by_events/?event_year=201%d/' %i for i in range(9, 7, -1)]

    def parse(self, response):
        events = response.xpath('//td[2]/a/@href').extract() 
        for event in events:
            item = LinkItem()
            #item['link'] = response.urljoin(event)

            #Generate csv download link
            event_num = response.urljoin(event)
            match = re.compile(r"(event=.*)").findall(event_num)
            item['download_link'] = 'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?' + ''.join(match)
            yield item