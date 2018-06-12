# -*- coding: utf-8 -*-
"""
-------------------------------------------------
          Author :  danny.pang
        File Name： details_items
             date： 2018/6/7
     Description :
-------------------------------------------------
   Change Activity: 2018/6/7
-------------------------------------------------
"""
__author__ = 'danny.pang'


import scrapy


class DetailsItem(scrapy.Item):
    id = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    store = scrapy.Field()
    goods_name = scrapy.Field()
    goods_code = scrapy.Field()
    goods_weight = scrapy.Field()
    goods_product_nation = scrapy.Field()
    goods_volume = scrapy.Field()
    goods_product_type = scrapy.Field()
    goods_style = scrapy.Field()
    goods_packaging = scrapy.Field()
    goods_scence = scrapy.Field()
