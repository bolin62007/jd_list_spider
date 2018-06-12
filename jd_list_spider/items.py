# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdListSpiderItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()

class JdIdListItem(scrapy.Item):
    id_list = scrapy.Field()


