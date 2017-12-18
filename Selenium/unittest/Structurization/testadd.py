#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 15:32
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 16:32
# @Author  : Soner
# @version :
# @license : Copyright(C), Your Company
from Selenium.unittest.calculator import Count
#from calculator import Count
import unittest

# 测试两个整数相加
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("=====初始化=====")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)    # 判断 j.add 的值是否等于5；assertTqual() 由 unittest 框架提供

    def test_add2(self):
        j = Count(212, 321)
        self.assertEqual(j.add(), 12312)

    def tearDown(self):
        print("=====清理环境=====")

if __name__ == '__main__':
    unittest.main()
