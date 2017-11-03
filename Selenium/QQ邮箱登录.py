#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version : 
@Time    : 2017/11/2/0002 12:01
@license : Copyright(C), Your Company 
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

mailurl = "https://mail.qq.com/"
driver.get(mailurl)

# 因为登录框是一个内嵌frame所以需要切换到这个内框中
driver.switch_to.frame("login_frame")

driver.find_element_by_class_name("switch_btn").click()
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("XXXXXXXXX")
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys("XXXXXXXX")
driver.find_element_by_id("login_button").click()

sleep(3)
driver.find_element_by_link_text("退出").click()

sleep(3)
driver.quit()