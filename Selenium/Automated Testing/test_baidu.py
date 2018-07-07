#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/29 11:07
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.baidu_url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.baidu_url)
        driver.find_element_by_id("k").send_keys("sorce")
        sleep(2)
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 定义报告存放的位置
    fp = open("F:/PyTest/Selenium/Automated Testing/result.html", "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="百度搜索测试报告",
                            description="用例执行情况：")
    runner.run(testunit)
    fp.close()
