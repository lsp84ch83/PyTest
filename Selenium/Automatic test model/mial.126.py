#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 16:07
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from .public import Login
from time import sleep

driver = webdriver.Chrome()
driver.get("http://mail.126.com")
driver.implicitly_wait(10)
driver.maximize_window()




driver.quit()


