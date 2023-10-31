#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/8/13 11:21
# @Author : jungle
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode('utf-8'))

# 获取一个post请求
# data = bytes(urllib.parse.urlencode({"error": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

# try:
#     response = urllib.request.urlopen("https://httpbin.org/get", timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheader("Server"),response.getheader("User-Agent"),response.getheaders())

# url = "http://httpbin.org/post"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/84.0.4147.125 Safari/537.36 "
# }
# data = bytes(urllib.parse.urlencode({"name": "jungle"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36 "
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
