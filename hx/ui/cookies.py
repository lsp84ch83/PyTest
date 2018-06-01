#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 18:15

__author__ = 'Soenr'

from selenium import webdriver
import json
import time

def ads():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://eam-dev.hollo.cn/")

    # 登录一次以便获取cookie
    driver.find_element_by_id("LAY-user-login-username").send_keys("lijun")
    driver.find_element_by_name("password").send_keys("111111")
    driver.find_element_by_id("js_login_submit_btn").click()

    time.sleep(5)

    # 获取cookie并通过json模块将dict转化成str
    dictCookies = driver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    # 登录完成后，将cookie保存到本地文件
    with open('cookies.json', 'w') as f:
        f.write(jsonCookies)

    # 初次建立连接，随后方可修改cookie
    # driver.get("http://eam-dev.hollo.cn/")
    # 删除第一次建立连接时的cookie
    driver.delete_all_cookies()
    # 读取登录时存储到本地的cookie
    with open('cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())

    for cookie in listCookies:
        driver.add_cookie({
            'domain': 'eam-dev.hollo.cn',  # 此处xxx.com前，需要带点
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    return cookie