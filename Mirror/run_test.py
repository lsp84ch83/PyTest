#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 11:11
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Anewnotest1(unittest.TestCase):
    # 初始化应用
    def setUp(self):
        # 获取手机的信息
        desired_caps = {
            'platformName': 'Android',  # 平台
            'platformVersion': '5.1',  # 版本号
            'deviceName': '192.168.103.101:5555',  # 设备名称
            'appPackage': 'com.youdao.note',  # 应用包名
            'appActivity': '.activity2.SplashActivity',  # Activity名
            'unicodeKeyboard': 'True',  # 防止键盘中文不能输入
            'resetKeyboard': 'True'  # 重置设置生效
        }
        # 启动appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(3)

