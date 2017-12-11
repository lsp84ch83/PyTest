#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# ------------------------------------------------------------------------------------------
'''
# --------------------------使用读取 csv 来获取账号密码，解决多字段读取--------------------------
'''
import csv

# 读取本地 csv 文件
my_file = open("userinfo.csv", "r")
date = csv.reader(my_file)

for user in date:
    print(user[0])  # 获取账号信息
    print(user[1] + "\n")  # 获取邮箱信息
# ---------------------------------------------------------------------------------
'''
