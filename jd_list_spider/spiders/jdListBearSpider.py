import scrapy
from urllib import request
import json
import string
from jd_list_spider.id_list_items import IdListItem


count = 1
default_get_price_url = 'http://p.3.cn/prices/mgets?type=1&pdpin=877735203_768111041&pduid=1527226008048409815180&skuIds='
default_get_comment_url = 'http://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds='
init_num = 1
base_url = 'http://list.jd.com/list.html?cat=9987,653,655&sort=sort_rank_asc&trans=1&page='
last_comfort = '&page=1&JL=6_0_0#J_main'
max_page_num = 5


current_base_url = 'http://list.jd.com/list.html?cat=12259,14716,15602&sort=sort_totalsales15_desc&trans=1&page='
current_last_url = '&JL=6_0_0#J_main'
class jdListBearSpider(scrapy.Spider):
    name = "jdListBearSpider"
    start_urls = [
        # 'http://list.jd.com/list.html?cat=12259,14716,15602&sort=sort_totalsales15_desc&trans=1&page=1&JL=6_0_0#J_main'
        current_base_url + str(init_num) + current_last_url
    ]
    def parse(self, response):
        print("clawlering: " + response.url)
        # get all id    ---> response.css('#plist > ul > li > div a::attr(data-sku)').extract()

        # 获取ids
        ids = response.css('#plist > ul > li > div a::attr(data-sku)').extract()
        # str1 = self.listToStr(ids)
        #
        # # 获取价格list
        # get_price_url = default_get_price_url + str1
        # priceList = self.getResult(get_price_url)
        id_list = json.dumps(ids)
        item = IdListItem()
        item['id_list'] = id_list
        yield item

        parseList = response.css('#plist > ul li.gl-item')
        #response.css('#J_topPage > span > b::text').extract_first()   d当前页码
        # response.css('#J_topPage > span >i::text').extract_first() 总页码
        # for index in range(len(parseList)):
        #     details = parseList[index]
        #     if type(details) is str:
        #         continue
        #
        #     id = details.css('div.j-sku-item::attr(data-sku)').extract_first().strip()
        #     item['price'] = self.getPriceById(priceList, id)
        #     item['name'] = details.css('.p-name em::text').extract_first().strip()
        #     yield item

        current_page_num = int(response.css('#J_topPage > span > b::text').extract_first())
        max_page_num = int(response.css('#J_topPage > span >i::text').extract_first())
        if current_page_num < max_page_num:
            # if current_page_num == 3:
            #     return
            next_page_num = current_page_num + 1
            next_url = current_base_url + str(next_page_num) + current_last_url
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

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

    def getPriceById(self, priceList, id):
        for i in priceList:
            if (i['id'])[2:] == id:
                return i['p']
        return -1
