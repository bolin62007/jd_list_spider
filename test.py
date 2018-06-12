# -*- coding: utf-8 -*-
"""
-------------------------------------------------
          Author :  danny.pang
        File Name： test
             date： 2018/6/11
     Description :
-------------------------------------------------
   Change Activity: 2018/6/11
-------------------------------------------------
"""
__author__ = 'danny.pang'

import json
from openpyxl import load_workbook

ss = 'sss9.4kg'
print(ss[-2:])


# 默认可读写，若有需要可以指定write_only和read_only为True
# wb = load_workbook('id_list.xlsx')
# sheet_name = wb.get_sheet_names()
# sheet = wb.get_sheet_by_name(sheet_name[0])
#
# array = []
# for column in sheet.columns:
#     for cell in column:
#         if(len(cell.value) > 3):
#             array.extend(json.loads(cell.value))
#
# print('before: ' + str(len(array)))
# array = list(set(array))
# print('after: ' + str(len(array)))
# print(array)
# import json
# list = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
# josnData = json.dumps(list) # '[1, 2, [3, 4]]'
# print(josnData)
# print(type(josnData))
