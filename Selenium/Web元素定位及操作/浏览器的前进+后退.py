#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/2/0002 10:57
@license : Copyright(C), Your Company 
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
sleep(1)
driver.get("http://news.baidu.com")
sleep(2)

driver.back() # 返回上一个网页，百度首页
sleep(2)

driver.forward() # 前进到下一个网页，百度新闻
sleep(2)

driver.quit()