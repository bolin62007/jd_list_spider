# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class DetailsPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append([
            '商品id',
            '价格',
            '品牌',
            '店铺',
            '商品名称',
            '商品编号',
            '商品毛重',
            '商品产地',
            '容量',
            '国产/进口',
            '分类',
            '包装',
            '适用场景',
        ])  # 设置表头

    def process_item(self, item, spider):
        rows = [
            item['id'],
            item['price'],
            item['name'],
            item['store'],
            item['goods_name'],
            item['goods_code'],
            item['goods_weight'],
            item['goods_product_nation'],
            item['goods_volume'],
            item['goods_product_type'],
            item['goods_style'],
            item['goods_packaging'],
            item['goods_scence'],
        ]  # 把数据中每一项整理出来
        self.ws.append(rows)  # 将数据以行的形式添加到xlsx中
        self.wb.save('detailx.xlsx')  # 保存xlsx文件
        return item