#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/18 16:16
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
# _*_ coding: utf-8 _*_
from selenium import webdriver
import unittest, time


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "python_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
