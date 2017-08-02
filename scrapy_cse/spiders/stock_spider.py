import scrapy
import json

class CompanySpider(scrapy.Spider):
    name = "company"
    url = 'https://www.cse.lk/api/alphabetical'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
    def start_requests(self):
        for letter in self.alphabet:
            yield scrapy.FormRequest(self.url, callback=self.parse, formdata={'alphabet': letter})

    def parse(self, response):
        resp = json.loads(response.body)
        for company in resp['reqAlphabetical']:
            print company['name']
            #yield company


