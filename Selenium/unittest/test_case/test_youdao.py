#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 16:16
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
import unittest, time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = ("http://fanyi.baidu.com")

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("baidu_translate_input").clear()
        driver.find_element_by_id("baidu_translate_input").send_keys("web driver")
        driver.find_element_by_id("translate-button").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "百度翻译")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
