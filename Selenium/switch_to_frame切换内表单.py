#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 15:52
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_url = "file:///" + os.path.abspath("frame.html")
driver.get(file_url)

# 切换到iframe内框; switch_to_frame() 默认可以直接取表单的 id 或 name 属性进行切换
driver.switch_to_frame('if')

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

# 返回上一层表单
driver.switch_to_default_content()

sleep(2)
driver.quit()