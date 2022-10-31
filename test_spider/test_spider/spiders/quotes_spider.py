import scrapy

from test_spider.items import YbItem


class QuotesSpider(scrapy.Spider):
    '''
    来源：中国银行研究院
    类型:报告
    推荐来源：凯恩斯-知识星球
    推荐理由：
    更新频率： 季频
    '''
    name = "zgyhyjybg"
    start_urls = ["https://www.bankofchina.com/fimarkets/summarize/"]

    def parse(self, response):
        # 提取网站title
        print(response.xpath("/html/body/div/div[5]/div/ul/li/a/@href").extract())
        list = response.xpath("/html/body/div/div[5]/div/ul/li/a/@href").extract()
        # 详情页内容
        for i in list:
            yield response.follow(i, callback=self.parse_detail)

        # print(response.xpath("//meta[@name='description']/@content").extract_first())
        # print("网站地址: ", response.url)
    def parse_detail(self, response):
        print(response.url)
        yb = YbItem()
        # 标题 //h2        
        print(response.xpath("//h2/text()").extract_first())
        yb['title'] = response.xpath("//h2/text()").extract_first()
        # 日期
        yb['date'] = response.xpath('//p[@class="con_time"]/text()').extract_first()
        # 作者
        yb['author'] = response.xpath('//p[align="center"]').extract_first()
        # 内容         
        yb['content'] = response.xpath("//div[@class='TRS_Editor']").extract_first()
        yb['sourse'] =response.url

        yield yb

    def parse_PDF(self, response):
        pass
