import scrapy
import os
import logging

class ToiSpider(scrapy.Spider):
    name = "tos"
    allowed_domains = ['indiatimes.com']
    start_urls = [
        "http://timesofindia.indiatimes.com/entertainment"

        ]
    links = []
    
    
    outdir = '' 
    #typical url 'http://timesofindia.indiatimes.com/tech/tech-news/title/articleshow/47827034.cms'
    def parse_callback(self, response):
        #self.open_links(response)

        if response.url.split('/')[-2] == 'articleshow':
            #all the valid posts
            title = response.url.split("/")[-3]
            filename = self.outdir + '/' + title + '.html'
            logging.warning("\n\n---------->"+filename)
            try:
                title =  response.xpath('//span[@class = "arttle"]/h1/text()').extract()[0]
                image = response.xpath('//div[@class = "mainimg1"]//img/@src').extract()[0]
                content = "\n".join(response.xpath('//div[@class = "Normal"]/text()').extract()) 
            except:
                return
            with open(filename, 'w') as f:
                f.write(title +"\n\n"+ image+"\n\n"+content)

    def parse(self, response):
        self.outdir = 'crawled/' + response.url.split("/")[-1]
        if not os.path.exists( self.outdir):
            os.makedirs(self.outdir)

        for href in response.xpath('//@href').extract():
            url = href
            if 'http' not in url:
                url = 'http://timesofindia.indiatimes.com' + url
            
            yield scrapy.Request(url, callback=self.parse_callback)
 

    

