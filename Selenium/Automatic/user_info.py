#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/11 17:19
# @Author  : Soner
# @version :
# @license : Copyright(C), Your Company
# ------------------------使用读取 txt 来获取账号密码，适用于双字段去读------------------------
'''
user_file = open("user_info.txt", "r")  # 打开user_info.txt 只读方式
values = user_file.readlines()  # 将user_file的内容全部按行赋给 values
user_file.close()   # 关闭user_info.txt 文件

for serch in values:
    username = serch.split(",")[0] # 每一行以"," 为分隔符取第0位元素 赋值给username
    print("账号：%s" % username)
    userpassword = serch.split(",")[1]
    print("密码：%s" % userpassword)
# -----------------------------------------------------------------------------------------

# --------------------------使用读取 csv 来获取账号密码，解决多字段读取-------------------------

import csv

# 读取本地 csv 文件
my_file = open("userinfo.csv", "r")
date = csv.reader(my_file)

for user in date:
    print(user[0])  # 获取账号信息
    print(user[1] + "\n")  # 获取邮箱信息
# -----------------------------------------------------------------------------------------
'''
# --------------------------使用读取 xml 来获取账号密码，解决不规则字段读取-------------------------
from xml.dom import minidom

dom = minidom.parse("info.xml")
# # 得到 XML 文件的唯一根元素
root = dom.documentElement
# print(root.nodeName)    # 输出节点名称
# print(root.nodeValue)   # 输出节点值
# print(root.nodeType)    # 输出节点类型
# print(root.ELEMENT_NODE)
# ------------1.获得任意标签名 getElementByTagName() 可以通过标签名获取标签------------
# tagname = root.getElementsByTagName('browser')
# print(tagname[0].tagName)
# tagname = root.getElementsByTagName("test_login")
# print(tagname[1].tagName)
# tagname = root.getElementsByTagName("province")
# print(tagname[2].tagName)

# ------------2.获得标签的属性值 getAttribute() 方法用千获取元素的属性值------------
# logins = root.getElementsByTagName("test_login")
# # 获得 logins 标签的 username 属性值
# username = logins[0].getAttribute("username")
# print(username)
# # 获得 logins 标的 password 属性值
# password = logins[0].getAttribute("password")
# print(password)

# ------------3.获得标签对之间的数据 firstChild 属性返回被选节点的第一个子节点; data 表示获取该节点的数据------------
provinces = dom.getElementsByTagName("province")
citys = dom.getElementsByTagName("city")
p2 = provinces[1].firstChild.data   # 获得第二个 province 标签对的值
print(p2)
c1 = citys[0].firstChild.data # 获得第一个 citys 标签对的值
print(c1)