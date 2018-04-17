#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 15:35
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from Selenium.unittest.calculator import Count
#from calculator import Count
import unittest

class TestSub(unittest.TestCase):
    def setUp(self):
        print("=====初始化=====")

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(11, 2)
        self.assertEqual(j.sub(), 12)

    def tearDown(self):
        print("=====清理环境=====")

if __name__ == '__main__':
    unittest.main()
