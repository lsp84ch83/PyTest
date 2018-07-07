#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/6/8 14:43
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from selenium.webdriver.common.by import By

def reg(driver, username, password, repassword):
    driver.find_element(By.LINK_TEXT,"注册").click()
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"repassword").send_keys(repassword)
    driver.find_element(By.CLASS_NAME,"input_submit").click()
