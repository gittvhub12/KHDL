import scrapy
import json
from scrapy.selector import Selector


class collect_player_url(scrapy.Spider):
  name='get_company' 
  
  def start_requests(self):
    yield scrapy.Request('https://www.forbes.com/lists/global2000', self.parse)

  def parse(self, response):
    for item in response.xpath('//*[@id="table"]/div[1]/div/div/a').getall():
        yield {"Rank": Selector(text=item).xpath('//div[1]/text()').get()[:-1],
              "Name": Selector(text=item).xpath('//div[2]/text()').get(),
              "Country": Selector(text=item).xpath('//div[3]/text()').get(),
              "Sales": Selector(text=item).xpath('//div[4]/text()').get(),
              "Profits": Selector(text=item).xpath('//div[5]/text()').get(),
              "Assets": Selector(text=item).xpath('//div[6]/text()').get(),
              "Market value": Selector(text=item).xpath('//div[7]/text()').get()
        }
