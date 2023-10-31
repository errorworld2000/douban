#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/8/13 21:05
# @Author : jungle
# @File : testXlwt.py
# @Software : PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
worksheet = workbook.add_sheet("sheet1")
worksheet.write(0, 0, "hello")  # 写入数据,行,列,内容
workbook.save("student.xls")
