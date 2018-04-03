#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 16:24
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import xlrd
import sys


class Ballnotest(unittest.TestCase):
    def setUp(self):
        # 获取手机的信息
        desired_caps = {
            'platformName': 'Android',  # 平台
            'platformVersion': '4.4',  # 版本号
            'deviceName': '192.168.103.101:5555',  # 设备名称
            'appPackage': 'com.youdao.note',  # 应用包名
            'appActivity': '.activity2.SplashActivity',  # Activity名
            'unicodeKeyboard': 'True',  # 防止键盘中文不能输入
            'resetKeyboard': 'True'  # 重置设置生效}
            }
        # 启动appium
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(3)

    def test_exchange(self):
        # 进入APP 截图
        driver = self.driver
        driver.get_screenshot_as_file(r'f:\PyText\Appium\appium-framwork\err_pic\err1.png')
        time.sleep(2)

        driver.find_element(By.NAME, '云笔记').click()
        driver.get_screenshot_as_file(r'f:\PyText\Appium\appium-framwork\err_pic\err2.png')
        time.sleep(2)

        driver.find_element(By.NAME, '云协作').click()
        driver.get_screenshot_as_file(r'f:\PyText\Appium\appium-framwork\err_pic\err3.png')
        time.sleep(2)

        driver.find_element(By.NAME, '我的').click()
        driver.get_screenshot_as_file(r'f:\PyText\Appium\appium-framwork\err_pic\err4.png')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


