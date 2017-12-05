#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 10:40
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

try:
    driver.find_element_by_id("kw1").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(2)
except:
    driver.get_screenshot_as_file("F:\\PyText\\Selenium\\baidu_err.jpg")

driver.quit()