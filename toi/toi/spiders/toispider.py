import scrapy
import os

class ToiSpider(scrapy.Spider):
    name = "toi"
    start_urls = [
        "http://timesofindia.indiatimes.com/tech/"
        ]
    
    #typical url 'http://timesofindia.indiatimes.com/tech/tech-news/title/articleshow/47827034.cms'
    def parse_callback(self, response):
        try:
            title, category = response.url.split("/")[-3], response.url.split("/")[-5]
            filename = 'crawled/' + category + '/' + title + '.html'
            title =  response.xpath('//span[@class = "arttle"]/h1/text()').extract()[0]
            image = response.xpath('//div[@class = "mainimg1"]//img/@src').extract()[0]
            content = "\n".join(response.xpath('//div[@class = "Normal"]/text()').extract()) 
        except:
            return
        with open(filename, 'w') as f:
            f.write(title +"\n\n"+ image+"\n\n"+content)


    def parse(self, response):
        links = []
        #crawled/tech or crawled/politics        
        directory = 'crawled/' + response.url.split("/")[-1]
        if not os.path.exists( directory):
            os.makedirs(directory)

        for href in response.xpath('//@href').extract():
            #if base url there in href
            if response.url in href:
                if href.split('?')[0] not in links:
                    links.append(href)
                    yield scrapy.Request(href, callback=self.parse_callback)

        with open('links','w') as f:
            f.write("\n".join(links))
