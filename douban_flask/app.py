#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/9/3 12:24
# @Author : jungle
# @File : app.py
# @Software : PyCharm

import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    datalist = []
    conn = sqlite3.connect('movie250.bd')
    cur = conn.cursor()
    sql = 'select * from movie250 limit 25'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('data.html', datalist=datalist)


@app.route('/data/start=25')
def data25():
    datalist = []
    conn = sqlite3.connect('movie250.bd')
    cur = conn.cursor()
    sql = 'select * from movie250 limit 25 offset 25'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('data.html', datalist=datalist)


if __name__ == '__main__':
    app.run(debug=True)
