import scrapy
from scrapy import Request
from urllib import request
import json
import string
import os
from jd_list_spider.details_items import DetailsItem
from openpyxl import load_workbook
# from urllib import request

count = 1
default_get_price_url = 'http://p.3.cn/prices/mgets?type=1&pdpin=877735203_768111041&pduid=1527226008048409815180&skuIds='
default_get_comment_url = 'http://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds='
init_num = 2763377
base_url = 'http://list.jd.com/list.html?cat=9987,653,655&sort=sort_rank_asc&trans=1&page='
last_comfort = '&page=1&JL=6_0_0#J_main'
max_page_num = 5

# http://item.jd.com/2763377.html
current_base_url = 'http://item.jd.com/'
current_last_url = '.html'

base_price_url = 'http://p.3.cn/prices/mgets?skuIds=J_'
class jdListBearSpider(scrapy.Spider):
    name = "detailsSpider"

    def start_requests(self):
        ids = self.getLIdsResult()
        start_urls = []
        for i in ids:
            # start_urls.extend(current_base_url + str(init_num) + current_last_url)
            url = current_base_url + i + current_last_url
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True)

    def parse(self, response):
        print("clawlering: " + response.url)

        goods_dist = response.css('div.p-parameter > ul.parameter2.p-parameter-list li::attr(title)').extract()

        id = response.url[19:-5]
        price_url = base_price_url + str(id)
        priceList = self.getResult(price_url)

        item = DetailsItem()
        item['id'] = id
        item['price'] = priceList[0]['p']
        item['name'] = response.css('#parameter-brand > li::attr(title)').extract_first()
        item['store'] = response.css('#popbox > div > div.mt > h3 > a::attr(title)').extract_first()
        item['goods_name'] = goods_dist[0]
        item['goods_code'] = goods_dist[1]
        # has nation

        if len(goods_dist) == 10:
            item['goods_product_nation'] = goods_dist[4]
            item['goods_weight'] = goods_dist[3]
            item['goods_volume'] = goods_dist[5]
            item['goods_product_type'] = goods_dist[6]
            item['goods_style'] = goods_dist[7]
            item['goods_packaging'] = goods_dist[8]
            item['goods_scence'] = goods_dist[9]
        elif len(goods_dist) == 11:
            item['goods_product_nation'] = goods_dist[4]
            item['goods_weight'] = goods_dist[3]
            item['goods_volume'] = goods_dist[6]
            item['goods_product_type'] = goods_dist[7]
            item['goods_style'] = goods_dist[8]
            item['goods_packaging'] = goods_dist[9]
            item['goods_scence'] = goods_dist[10]
        else:
            if goods_dist[2][-2:] == 'kg':
                item['goods_product_nation'] = goods_dist[3]
                item['goods_weight'] = goods_dist[2]
            else:
                # no nation
                item['goods_product_nation'] = ''
                item['goods_weight'] = goods_dist[3]
            item['goods_volume'] = goods_dist[4]
            item['goods_product_type'] = goods_dist[5]
            item['goods_style'] = goods_dist[6]
            item['goods_packaging'] = goods_dist[7]
            item['goods_scence'] = goods_dist[8]
        yield item

    def getResult(self, get_price_url):
        res = request.urlopen(get_price_url)
        priceList = json.loads(res.read().decode('utf-8'))
        return priceList

    def getLIdsResult(self):
        folder = os.path.abspath('.')
        xlsx_path = os.path.join(folder, 'id_list.xlsx')
        wb = load_workbook(xlsx_path)
        sheet_name = wb.get_sheet_names()
        sheet = wb.get_sheet_by_name(sheet_name[0])

        array = []
        for column in sheet.columns:
            for cell in column:
                if (len(cell.value) > 3):
                    array.extend(json.loads(cell.value))

        array = list(set(array)) # list 去重
        print('array: ' + str(len(array)))
        return array