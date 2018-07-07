#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/14 16:32
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
from Selenium.unittest.calculator import Count
#from calculator import Count
import unittest

# 将setUp 和 tearDown 封装成一个类
class MyTest(unittest.TestCase):
    def setUp(self):
        print("=====初始化=====")
    def tearDown(self):
        print("=====清理环境=====")
# 测试两个整数相加
class TestAdd(MyTest):
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)    # 判断 j.add 的值是否等于5；assertTqual() 由 unittest 框架提供

    def test_add2(self):
        j = Count(212, 321)
        self.assertEqual(j.add(), 12312)

class TestSub(MyTest):

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(11, 2)
        self.assertEqual(j.sub(), 12)

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))  # 添加测试用例
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

'''
首先，调用 unittest 框架的 TestSuite() 类来创建测试套件，
通过它所提供的 addTest()方法来添加测试用例 test_add2(),
接着调用 unittest 框架的 TextTestRunner()类，通过它下面run()方法来运行 suite 所组装的测试用例
'''
