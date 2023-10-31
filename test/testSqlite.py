#!/usr/bin/env python3
# -*- coding = utf-8 -*-
# @Time : 2020/8/13 21:38
# @Author : jungle
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()
# sql='''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''

# sql1 = '''
#     insert into company(id,name,age,address,salary)
#     values(10,'张三',33,'成都',8000);
# '''
#
# c.execute(sql1)

sql = "select id,name,address,salary from company"
cursor = c.execute(sql)
for row in cursor:
    print("id=", row[0])
    print("name=", row[1])
    print("address=", row[2])
    print("salary=", row[3], "\n")
# conn.commit()
conn.close()
