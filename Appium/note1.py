#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 11:12
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company


from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 获取手机信息 -- 并存到字典中
desired_caps = {
    'platformName' : 'Android',     # 平台
    'platformVersion' : '4.4',    # 版本号
    'deviceName' : '192.168.103.101:5555',  # 设备名称
    'appPackage' : 'com.youdao.note',   # 应用包名
    'appActivity' : '.activity2.SplashActivity',   # Activity名
    'unicodeKeyboard' : 'True',     # 防止键盘中文不能输入
    'resetKeyboard' : 'True'   # 重置设置生效
}

# 启动 appium ，将手机信息导入
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)

'''
# 新建笔记
driver.find_element_by_id('com.youdao.note:id/add_note_floater_open').click()
# 选择新建笔记
driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()

# 输入笔记名称
driver.find_element_by_id('com.youdao.note:id/note_title').send_keys("Text")
# 输入笔记内容
driver.find_element_by_class_name('android.widget.EditText').send_keys('编辑内容')
# 保存笔记
driver.find_element_by_id('com.youdao.note:id/actionbar_complete_text').click()
'''

# 推荐By.ID
# 新建笔记
driver.find_element(By.ID,'com.youdao.note:id/add_note_floater_open').click()
# 选择新建笔记
driver.find_element(By.NAME, '新建笔记').click()

# 输入笔记名称
driver.find_element(By.ID, 'com.youdao.note:id/note_title').send_keys("Text")
# 输入笔记内容
driver.find_element(By.XPATH, '//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]').send_keys('编辑内容')
# 保存笔记
driver.find_element(By.NAME, '完成').click()

driver.quit()