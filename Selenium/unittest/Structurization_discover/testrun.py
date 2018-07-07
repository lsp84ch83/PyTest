#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/12/15 15:55
# @Author  : Soner
# @version : 
# @license : Copyright(C), Your Company
import unittest

test_dir = r'f:\PyTest\Selenium\unittest'
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir= test_dir)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)

'''
discover(start_dir, pattem='test*.py',  top_level_dir=None) 
    找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件
名才能被加载。如果启动的不是顶层目录，那么顶层目录必须单独指定，另外有测试案例的目录里必须有__init__.py文件，否则会找不到
 
•  start_dir:  要测试的模块名或测试用例目录, 当前目录用'./'表示
•  pattem='test*.py':  表示用例文件名的匹配原则。此处匹配文件名以"test"开头的".py"类型的文件，星号"*"表示任意多个字符
•  top_level_dir=None: 测试模块的顶层目录，如果没有顶层目录，默认为 None; 如果有顶层目录应为test_dir
'''