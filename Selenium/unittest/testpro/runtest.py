#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/15 15:37
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
import unittest

from Selenium.unittest.testpro import testadd
from Selenium.unittest.testpro import testsub

# 构造测试集
suite = unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testsub.TestSub("test_sub"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__ == "__main__":
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)