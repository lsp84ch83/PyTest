#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@File    : doutuapp.py
@version : 
@Time    : 2017/10/29/0029 21:54
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
# flask:Python中轻量级web框架
from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route("/search")
def search():
    kw =request.args.get("kw") # 获取用户的get请求的参数和值
    count = request.args.get("count")
    cursor.execute("select * from images where `name` like '%{}%'".format())
    data = cursor.fetchmany(int(count))
    return render_template('index.html', images=data)



if __name__ =='__main__':
    conn= pymysql.connect(
        host="mysql.litianqing.com",
        port=7150,
        user="test11",
        passwd="123456",
        db="test11",
        charset="utf8",
        cursorclass=pymysql.cursor.DictCursor,

    )
    app.run(debug=True)