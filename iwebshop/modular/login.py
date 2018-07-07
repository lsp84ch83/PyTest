#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/6/8 13:51
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from selenium.webdriver.common.by import By

def login(driver, username, password):
    driver.find_element(By.LINK_TEXT,"登录").click()
    driver.find_element(By.NAME,"login_info").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.CLASS_NAME,"input_submit").click()