import scrapy

class ToiSpider(scrapy.Spider):
    name = "toi"
    start_urls = [
        "http://timesofindia.indiatimes.com/tech/tech-news/MF-agents-guaranteed-returns-to-Flipkart-violate-Sebi-norms/articleshow/47823478.cms"
        ]

    def parse(self, response):
        filename = response.url.split("/")[-3] + '.html'
        with open(filename, 'w') as f:
            #f.write(response.body)
            title =  response.xpath('//span[@class = "arttle"]/h1/text()').extract()[0]
            image = response.xpath('//div[@class = "mainimg1"]//img/@src').extract()[0]
            content = "\n".join(response.xpath('//div[@class = "Normal"]/text()').extract()) 
            f.write(title +"\n\n"+ image+"\n\n"+content)
