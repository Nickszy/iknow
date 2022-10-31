# spiders/quotes.py

import scrapy
from test_spider.items import TestSpiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = TestSpiderItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
