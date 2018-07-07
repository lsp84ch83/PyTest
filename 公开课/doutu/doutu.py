#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : doutu.py
@version : 
@Time    : 2017/10/29/0029 21:03
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
import requests
import re
import pymysql

db = pymysql.connect(
    host = 'mysql.litianqiang.com',
    port=7150,
    user='test11',
    passwd='123456',
    db='test11',
    charset='utf8',
)
cursor = db.cursor()

def getImagesList():
    res = requests.get("http://www.doutula.com/photo/list/?page={}")
    html = res.text
    reg = r"data-original='(.*?)'.*?alt='(.*?)'"
    imagesList = re.findall(reg, html)
    for i in imagesList:
        # i=('http://XXX', '哈哈')
        cursor.execute("insert_into_images(`name`,imageUrl) value('{}', '{}')".format(i[1], i[0])) #执行sql语句
        db.commint()

for i in range(1,1084):
    getImagesList(i)


getImagesList()
db.close()