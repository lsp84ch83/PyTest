#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 16:24
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import xlutils,xlrd,xlwt

class Anewnotest1(unittest.TestCase):
    # setUp 初始化
    def setUp(self):
        # 获取手机的信息
        desired_caps = {
            'platformName': 'Android',  # 平台
            'platformVersion': '4.4',  # 版本号
            'deviceName': '192.168.103.101:5555',  # 设备名称
            'appPackage': 'com.youdao.note',  # 应用包名
            'appActivity': '.activity2.SplashActivity',  # Activity名
            'unicodeKeyboard': 'True',  # 防止键盘中文不能输入
            'resetKeyboard': 'True'  # 重置设置生效
        }
        # 启动appium
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)


    def test_newnote(self):
        driver = self.driver
        # 读取excel
        wb = xlrd.open_workbook(r'f:\PyText\Appium\appium-framwork\data\data.xls')
        sh = wb.sheet_by_name('note')
        r_num = sh.nrows

        # 循环读取
        for i in range(1, r_num):
            id - sh.cell_value(i, 0)
            title = sh.cell_value(i, 1)
            content = sh.cell_value(i, 2)
            result = sh.cell_value(i, 3)
            sleep(3)

            # 新建笔记
            driver.find_element(By.ID, 'com.youdao.note:id/add_note_floater_open').click()
            # 选择新建笔记
            driver.find_element(By.NAME, '新建笔记').click()

            # 输入笔记名称
            driver.find_element(By.ID, 'com.youdao.note:id/note_title').send_keys(title)
            # 输入笔记内容
            driver.find_element(By.XPATH,
                                '//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]').send_keys(
                content)

            # 保存笔记
            driver.find_element(By.NAME, '完成').click()

            # 验证
            if title == '':
                res1 = driver.find_element(By.ID, 'com.youdao.note:id/title').text
                res2 = driver.find_element(By.ID, 'com.youdao.note:id/summary').text
                if res1 == res2:
                    print('success')
                else:
                    print('fail')
            elif result == 'ok':
                if driver.find_element(By.NAME, title) and driver.find_element(By.NAME, content):
                    print("success")
                else:
                    print("fail")

    def tearDown(self):
        self.driver.quit()