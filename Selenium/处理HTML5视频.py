#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 11:12
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐性等待页面元素加载时间
driver.get("http://videojs.com/")

video = driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 播放视频
print("START")
driver.execute_script("return arguments[0].play()", video)

# 播放15秒
sleep(15)

# 暂停视频
print("STOP")
driver.execute_script("arguments[0].pause()", video)

driver.quit()