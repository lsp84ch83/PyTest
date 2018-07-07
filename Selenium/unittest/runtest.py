#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/18 16:17
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
import unittest

test_dir = r'f:\PyTest\Selenium\unittest\test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)