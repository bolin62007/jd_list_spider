import scrapy
from urllib import request
import json
import string
from jd_list_spider.items import JdListSpiderItem


count = 1
default_get_price_url = 'http://p.3.cn/prices/mgets?type=1&pdpin=877735203_768111041&pduid=1527226008048409815180&skuIds='
default_get_comment_url = 'http://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds='
init_num = 1;
base_url = 'http://list.jd.com/list.html?cat=9987,653,655&sort=sort_rank_asc&trans=1&page='
last_comfort = '&page=1&JL=6_0_0#J_main'
max_page_num = 5

class jdListSpider(scrapy.Spider):
    name = "jdListSpider"
    start_urls = [
        # 'http://list.jd.com/list.html?cat=12259,14716,15602&page=3&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        base_url + str(init_num) + last_comfort
    ]
    def parse(self, response):
        print("clawlering: " + response.url)
        # get all id    ---> response.css('#plist > ul > li > div a::attr(data-sku)').extract()

        # 获取ids
        ids = response.css('#plist > ul > li > div a::attr(data-sku)').extract()
        str1 = self.listToStr(ids)
        commentStr = self.listToStrComments(ids)

        # 获取价格list
        get_price_url = default_get_price_url + str1
        priceList = self.getResult(get_price_url)

        # get_comment_url = default_get_comment_url + commentStr
        # commentList = self.getResult(get_comment_url)

        item = JdListSpiderItem()

        parseList = response.css('#plist > ul li.gl-item')

        for index in range(len(parseList)):
            details = parseList[index]
            if type(details) is str:
                continue
            item['J_price'] = priceList[index]['p']
            item['name'] = details.css('.p-name em::text').extract_first().strip()
            item['comment_count'] = ""
            item['merchant'] = details.css('.p-shop::attr(data-shop_name)').extract_first().strip()
            yield item

        # next_page_num = int(response.url[-1]) + 1
        # if next_page_num <= max_page_num:
        #     next_url = base_url + str(next_page_num) + last_comfort
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

    def listToStr(self, ids):
        sign = "%2CJ_"
        str1 = ''.join((sign + str(e)) for e in ids)
        str1[5:]
        return str1

    def listToStrComments(self, comments):
        str1 = ''.join((str(e) + ',') for e in comments)
        str1[:-1]
        return str1

    def getResult(self, get_price_url):
        res = request.urlopen(get_price_url)
        priceList = json.loads(res.read().decode('utf-8'))
        return priceList
