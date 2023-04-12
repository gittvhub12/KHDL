import scrapy
import json


class collect_company_url(scrapy.Spider):
  name='urls_company' 
  
  def start_requests(self):
    yield scrapy.Request('https://www.forbes.com/lists/global2000', self.parse)

  def parse(self, response):
    for item in response.xpath('//*[@id="table"]/div[1]/*/div/a/@href').getall():
        yield {"Url": item}