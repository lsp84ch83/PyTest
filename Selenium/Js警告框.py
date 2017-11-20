#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 14:47
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://wwww.baidu.com")

# 鼠标在“设置”处悬停
link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()
sleep(1.5)
# 打开搜索设置
driver.find_element_by_class_name("setpref").click()
# 保存设置
driver.find_element_by_css_selector("#gxszButton > a.prefpanelgo").click()