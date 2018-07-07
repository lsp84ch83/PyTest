#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/28 15:38
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from Mirror.data.basecase import BasecaseClass
from Mirror.interface.business_test import Business

class User_logn(Business):
    def setUp(self):
        Business.setUp(self)

    def tearDown(self):
        Business.tearDown(self)

    def test_user_all_null(self):
        ''' 登录信息为空 '''
        Business.test_guide_purchase(self)
        # 点击票夹跳转登录
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/bottom_bar_action_button').click()
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_phone').send_keys('')
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_password').send_keys('')
        TouchAction(self.driver).tap(x=661, y=768).perform() # 收起键盘
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/bt_confirm').click()
        sleep(3)
        self.assertEqual("登录",self.driver.find_element(By.ID,'cn.com.haoluo.www:id/title').text)