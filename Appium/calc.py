#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/3/31 13:55
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium import webdriver
from time import sleep

'''
# 获取手机信息 -- 并存到字典中
desired_caps = {}

desired_caps['platformName'] = 'Android' # 平台名称
desired_caps['platformVersion'] = '4.4.4'  # Android版本
desired_caps['deviceName'] = '192.168.103.101:5555' # 设备名称
desired_caps['appPackage'] = 'com.android.calculator2'    # 包名; 1. adb shell 进入手机shell  2. cd /data/data 进入存放程序的地方
desired_caps['appActivity'] = '.Calculator'   # 存放Activity名称
'''
desired_caps = {
    "platformName" : "Android",     # 平台
    "platformVersion" : "5.1",    # 版本号
    "deviceName" : "192.168.103.101:5555",  # 设备名称
    "appPackage" : "com.android.calculator2",   # 应用包名
    "appActivity" : ".Calculator"   # Activity名
}


# 启动 appium， 将手机信息导入
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)

# 定位 4+5 =9
# 4id：com.android.calculator2:id/digit4
driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
# + desc: 描述puls
driver.find_element_by_name('加').click()
# 5
driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
# =
driver.find_element_by_id('com.android.calculator2:id/eq').click()
# 结果 class class_name
result = driver.find_element_by_class_name('android.widget.EditText').text
print(result)

if  int(result) == 9:
    print('测试通过')
    driver.find_element_by_id('com.android.calculator2:id/clr').click()
else:
    print('测试不通过')

# 关闭计算器应用
sleep(3)
driver.quit()

