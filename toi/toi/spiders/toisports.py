import scrapy
import os
import logging

class ToiSpider(scrapy.Spider):
    name = "tos"
    allowed_domains = ['indiatimes.com']
    start_urls = [
        "http://timesofindia.indiatimes.com/sports/"
        ]
    links = []
    links_valid = []
        
    #typical url 'http://timesofindia.indiatimes.com/tech/tech-news/title/articleshow/47827034.cms'
    def parse_callback(self, response):
        #self.open_links(response)

        if response.url.split('/')[-2] == 'articleshow':
            self.links_valid.append(response.url)
            logging.warning("----->"+response.url)



    def parse(self, response):
        for href in response.xpath('//@href').extract():
            url = href
            if 'http' not in url:
                url = 'http://timesofindia.indiatimes.com' + url
            
            yield scrapy.Request(url, callback=self.parse_callback)
 

    

