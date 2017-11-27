#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 14:49
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
import time

#访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小,注意后面用的元素是否在这个大小内能找到
driver.set_window_size(600, 600)
'''
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
'''
# 使用Js元素聚焦点击元素 arguments[0] 代表找到的 target 元素
driver.find_element_by_id("kw").send_keys("selenium")
target = driver.find_element_by_id("su")
driver.execute_script("arguments[0].click()", target)

#将页面滚动条拖到底部
js = "window.scrollTo(300, 450)"
#js = "var q=document.body.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

driver.quit()