#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/8/13 10:51
# @Author : jungle
# @File : spider.py
# @Software : PyCharm

import re  # 正则表达式,进行文字匹配
import urllib.error  # 制定URL,获取网页数据
import urllib.request
import xlwt  # 进行excel操作
from bs4 import (BeautifulSoup)  # 网页解析,获取数据
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "movie250.bd"
    # saveData(datalist, savepath)
    saveDb(datalist, dbpath)
    askURL(baseurl)


# 影片链接规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片规则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含其中re.compile.
# 影片片名规则
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分规则
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudgeNum = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):  # 爬取网页
    datalist = []
    for i in range(0, 10):  # 不包含10
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取的网页
        #  逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if len(titles) >= 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudgeNum, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉br
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())  # 去掉空格

            datalist.append(data)
    # print(datalist)
    return datalist


# 得到特定的一个URL网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.125 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveData(datalist, savepath):  # 保存数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("sheet", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "电影中文名", "电影外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def saveDb(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)''' % ",".join(data)
        # print(sql)
        c.execute(sql)
        conn.commit()
    c.close()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    main()  # 调用函数
    print("爬取完毕!")
