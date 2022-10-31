import time
import scrapy
from scrapy_playwright.page import PageMethod

class ZhhuobizhengceSpider(scrapy.Spider):
    name = 'ZhHuobizhengce'
    # allowed_domains = ['www.pbc.gov.cn']
    
    def start_requests(self):
        print('dsadsaas')
        start_urls = 'http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/index.html'
        yield scrapy.Request(start_urls,    
                        meta={"playwright": True, "playwright_include_page": True,"errback":self.errback})
    
    def parse(self, response):
        time.sleep(2)
        print(response.text)
        page = response.meta["playwright_page"]
        print(response.meta)
        screenshot = page.screenshot(path="sdaasdsexample.png", full_page=True)
        # screenshot contains the image's bytes
        # page.close()
    
    def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        page.close()
# class ClickAndSavePdfSpider(scrapy.Spider):
#     name = "pdf"

#     def start_requests(self):
#         yield scrapy.Request(
#             url="https://example.org",
#             meta=dict(
#                 playwright=True,
#                 playwright_page_methods={
#                     "click": PageMethod("click", selector="a"),
#                     "pdf": PageMethod("pdf", path="/tmp/file.pdf"),
#                 },
#             ),
#         )

#     def parse(self, response):
#         pdf_bytes = response.meta["playwright_page_methods"]["pdf"].result
#         with open("iana.pdf", "wb") as fp:
#             fp.write(pdf_bytes)
#         yield {"url": response.url}  # response.url is "https://www.iana.org/domains/reserved"