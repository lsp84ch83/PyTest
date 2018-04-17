#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 10:51
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

# 指定测试用例目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if  __name__ == '__main__':
    test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='发布会签到系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    runner.run(discover)
    fp.close()