#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/20 11:56
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://wwww.baidu.com")

# 获得当前窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text("登录").click()
sleep(1.5)
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        # 切换到注册窗口
        driver.switch_to_window(handle)
        print("注册窗口")
        driver.find_element_by_name("userName").send_keys("text")
        driver.find_element_by_name("phone").send_keys("13321256523")
sleep(1.5)

for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to_window(handle)
        print("百度首页")
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("Selenium")
        driver.find_element_by_id("su").click()

sleep(2)
driver.quit()
