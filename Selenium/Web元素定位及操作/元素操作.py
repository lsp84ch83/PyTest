#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/2/0002 11:48
@license : Copyright(C), Your Company 
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)
# 返回百度底部备案信息
text = driver.find_element_by_id("cp").text
print(text)
# 返回元素的属性值，可以是id、name、type或元素拥有的其它任意属性
attribute = driver.find_element_by_id("kw").get_attribute('class')
print(attribute)
# 返回元素的结果是否可见，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)


# 定位到输入框
driver.find_element_by_id("kw").send_keys("Python")
# 定位到确认按钮
driver.find_element_by_id("su").click()
sleep(1)

# 清除文本输入框内容
driver.find_element_by_id("kw").clear()
sleep(1)
driver.find_element_by_id("kw").send_keys("selenium")

sleep(2)
driver.quit()