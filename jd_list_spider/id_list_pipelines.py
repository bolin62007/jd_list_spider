# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class IdListPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append([
            '价格'
        ])  # 设置表头

    def process_item(self, item, spider):
        rows = [
            item['id_list']
        ]  # 把数据中每一项整理出来
        self.ws.append(rows)  # 将数据以行的形式添加到xlsx中
        self.wb.save('id_list.xlsx')  # 保存xlsx文件
        return item