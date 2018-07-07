#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/5 13:58
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
"""
WebDriver 操作 cookie 的方法：
•  get_cookies():  获得所有 cookie 信息。
•  get_cookie(name):  返回字典的 key 为 "name" 的 cookie 信息。
•  add_ cookie(cookie_  diet):  添加 cookie, "cooki e_di ct" 指字典对象，必须有 name 和 value 值。
•  delete_cookie(name,optionsString):  删除 cookie 信息。
        "name" 是要删除的 cook记的名称
        "optionsString" 是该 cookie 的选项， 目前支持的选项包括“路径" .“域” 。
•  delete_ all_ cookies():  删除所有 cooki e 信息。
"""
from selenium import webdriver
import json
from time import sleep

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com")

# 登录一次以便获取cookie
driver.find_element_by_xpath('//*[@id="test_login-middle"]/div/div[6]/div[2]/a').click()
driver.find_element_by_name("userName").send_keys("username")   # 更换成自己的账号
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("password")     # 更换成自己的密码
driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()

# 获取cookie并通过json模块将dict转化成str
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
#print(jsonCookies)
# 初次建立连接，随后方可修改cookie
driver.get("http://pan.baidu.com")
# 删除第一次建立连接时的cookie
driver.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    driver.add_cookie({
        'domain': '.baidu.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })
sleep(3)
# 再次访问页面，便可实现免登陆访问
driver.get('http:pan.baidu.com')

driver.quit()