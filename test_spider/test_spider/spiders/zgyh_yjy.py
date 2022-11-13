import scrapy

from test_spider.items import YbItem
from scrapy.http import Request

class QuotesSpider(scrapy.Spider):
    '''
    来源：中国银行研究院
    类型:报告
    推荐来源：凯恩斯-知识星球
    推荐理由：
    更新频率： 季频
    '''
    name = "zgyhyjybg"
    def start_requests(self):
        start_urls = "https://www.bankofchina.com/fimarkets/summarize/"
        yield Request(start_urls, meta={"playwright": True})
        
    def parse(self, response):
        # 提取网站title
        # print(response.xpath("/html/body/div/div[5]/div/ul/li/a/@href").extract())
        list = response.xpath("/html/body/div/div[5]/div/ul/li/a/@href").extract()
        # 详情页内容
        for i in list:
            yield response.follow(i, callback=self.parse_detail)
        
        other_page = response.xpath('/html/body/div/div[5]/div/div/ol/li[7]/a/@href').extract_first()
        # print(other_page,response.urljoin(other_page),response.url)
        if response.url != response.urljoin(other_page):
            yield response.follow(other_page, callback=self.parse, meta={"playwright": True})

    #     # print(response.xpath("//meta[@name='description']/@content").extract_first())
    #     # print("网站地址: ", response.url)
    def parse_detail(self, response):
        # print(response.url)
        yb = YbItem()
        # 标题 //h2        
        # print(response.xpath("//h2/text()").extract_first())
        yb['title'] = response.xpath("//h2/text()").extract_first()
        # 日期
        yb['date'] = response.xpath('//p[@class="con_time"]/text()').extract_first()
        # 机构
        yb['institution'] = '中国银行研究院'
        # 作者
        yb['author'] = response.xpath("//div[@class='sub_con']//p[contains(text(),'作者') or contains(text(),'作 者')]/text()").extract_first()
        # 内容         
        yb['content'] = response.xpath('//div[@class="sub_con"]').extract_first()
        # 来源
        yb['source'] =response.url
        

        yield yb

    def parse_PDF(self, response):
        pass
