import scrapy
import json
import re

class collect_company_info(scrapy.Spider):
  name='company_infor'
  
  def __init__(self):
    try:
      with open('dataset/urls_company.json') as f:
        self.company = json.load(f)
      self.company_count = 1
    except IOError:
      print("File not found")


  def start_requests(self):
    urls = ['https://www.forbes.com/companies/berkshire-hathaway/?list=global2000']

    for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
      yield{
            "Name" : response.xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/h1/text()").getall()
      }

      if self.company_count < len(self.company):
        next_page_url = self.company[self.company_count]['Url']
        self.company_count += 1
        yield scrapy.Request(url=next_page_url, callback=self.parse)