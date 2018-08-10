#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/28 14:23
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company
# 手机驱动配置信息

from appium import webdriver
import unittest

class BasecaseClass(unittest.TestCase):

    def smtUP(self):
        # 获取手机的信息
        desired_caps = {
            'platformName': 'Android',  # 平台
            'platformVersion': '5.1',  # 版本号
            'deviceName': 'U8LFIJFA99999999',  # 设备名称
            'appPackage': 'cn.com.haoluo.www',  # 应用包名
            'appActivity': '.ui.LauncherActivity',  # Activity名
            'unicodeKeyboard': 'True',  # 防止键盘中文不能输入
            'resetKeyboard': 'True'  # 重置设置生效
        }

        # 启动appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tmarDown(self):
        self.driver.quit()
