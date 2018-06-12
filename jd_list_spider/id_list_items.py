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


class IdListItem(scrapy.Item):
    id_list = scrapy.Field()
