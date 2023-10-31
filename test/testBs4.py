#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/8/13 15:23
# @Author : jungle
# @File : testBs4.py
# @Software : PyCharm

from bs4 import BeautifulSoup

file = open("baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# print(bs.name)
#
# print(type(bs.head))  # 标签类型
# print(type(bs.a.string))  # 评论类型
# print(type(bs.title.string))  # 标签内容类型
# print(type(bs))  # 表示整个文档
#
# print(bs.title)
# print(bs.title.string)
# print(bs.a)
# print(bs.a.attrs)  # attrs

# ------------------------------------------

# 文档遍历

# print(bs.head.contents)
# print(bs.head.contents[1])

# 文档搜索

# (1)find_all()
# t_list=bs.find_all("a")

# 正则表达式:search()
# t_list=bs.find_all(re.compile("a"))
# t_list=bs.find_all(text=re.compile("\d"))

# 传入一个函数搜索
# def name_is_exits(tag):
#     return tag.has_attr("name")
# t_list =bs.find_all(name_is_exits)


# kwargs关键词参数
# t_list = bs.find_all(class_=True)

# text参数
# t_list = bs.find_all(text=["新闻", "地图", "贴吧"])

# limit参数
# t_list = bs.find_all("a",limit=3)

# CSS选择器
# t_list = bs.select(".mnav")
# t_list = bs.select("a[class='bri']")
# t_list = bs.select("head>title")

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())
for item in t_list:
    print(item)
