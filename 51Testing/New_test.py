#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/7 10:39
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

op = webdriver.ChromeOptions()
op.add_argument('disable-infobars')
driver = webdriver.Chrome(options=op)

driver.get("http://www.12306.cn/mormhweb")
sleep(4)

js = "document.getElementsByClassName('k2')[0].target='';"
driver.execute_script(js)
sleep(3)

driver.find_element(By.CLASS_NAME, "k2").click()


