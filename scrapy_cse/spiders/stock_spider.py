import scrapy
import json


class StockSpider(scrapy.Spider):
    name = "stocks"

    def start_requests(self):
        url = 'https://www.cse.lk/api/alphabetical'
        yield scrapy.FormRequest(url, callback=self.parse, formdata={'alphabet': 'A'})

    def parse(self, response):
        resp = json.loads(response.body)
        for company in resp['reqAlphabetical']:
            #print company
            yield company

        '''next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)'''