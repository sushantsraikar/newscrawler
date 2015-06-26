import scrapy

class ToiSpider(scrapy.Spider):
    name = "toi"
    start_urls = [
        "http://timesofindia.indiatimes.com/tech/"
        ]
    
    def parse_callback(self, response):
        filename = 'crawled/' + response.url.split("/")[-3] + '.html'
        with open(filename, 'w') as f:
            #f.write(response.body)
            title =  response.xpath('//span[@class = "arttle"]/h1/text()').extract()[0]
            image = response.xpath('//div[@class = "mainimg1"]//img/@src').extract()[0]
            content = "\n".join(response.xpath('//div[@class = "Normal"]/text()').extract()) 
            f.write(title +"\n\n"+ image+"\n\n"+content)


    def parse(self, response):
        links = []
        for href in response.xpath('//@href').extract():
            links.append(href)
        with open('links','w') as f:
            f.write("\n".join(links))
