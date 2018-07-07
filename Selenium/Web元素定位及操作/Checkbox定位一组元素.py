#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/3/0003 16:32
@license : Copyright(C), Your Company 
'''
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = "file://" + os.path.abspath("Checkbox.html")
driver.get(file_path)

'''
# 通过元素判断查找复选框
inputs = driver.find_elements_by_tag_name("input")
for i in inputs:
    if i.get_attribute("type") == "checkbox":
        i.click()
    sleep(2)
'''
'''
# 通过Xpath查找复选框
checks = driver.find_elements_by_xpath("//input[@type='checkbox']")
for check in checks:
    check.click()
    sleep(1.5)
'''
# 通过CSS查找复选框
checkboxes = driver.find_elements_by_css_selector("input[type=checkbox]")
for checkbox in checkboxes:
    checkbox.click()
    sleep(1.5)
# 打印当前页面type=checkbox的个数
print(len(checkboxes))

# 取消最后一个type=checkbox的复选框
# pop 函数用于获取列表中的一个元素，默认为最后一个(-1);(0)为获取第一个元素
driver.find_elements_by_css_selector("input[type=checkbox]").pop().click()

sleep(1)
driver.quit()