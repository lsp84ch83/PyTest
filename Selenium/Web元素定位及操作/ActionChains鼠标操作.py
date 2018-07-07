#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@version : 
@Time    : 2017/11/2/0002 14:43
@license : Copyright(C), Your Company 
'''
from selenium import webdriver
# 引入鼠标控制 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
'''
# 定位到需要右键的元素，赋值给一个变量接收
right_click = driver.find_element_by_name("tj_trnews")
# 对定位的元素进行右键操作
ActionChains(driver).context_click(right_click).perform()

# 定位到需要悬停的元素，赋值给一个变量接收
above = driver.find_element_by_link_text("设置")
# 对定位的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

# 定位到可以双击的元素，赋值给一个变量接受
double_click = driver.find_element_by_id("cp")
# 对定位的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()
'''

sleep(2)
driver.quit()