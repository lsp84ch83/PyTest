#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 13:49
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from selenium import webdriver
import time

def open():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://192.168.112.132:8888/iwebshop/")
    time.sleep(2)

    return driver