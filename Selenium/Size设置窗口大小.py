#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version : 
@Time    : 2017/11/1/0001 16:20
'''
from selenium import webdriver
import time

driver =  webdriver.Chrome()
driver.get("http://www.baidu.com")

# 参数设置为像素点
driver.set_window_size(480,800)
# driver.maximize_window() 将窗口设置为最大化
time.sleep(2)

driver.quit()