#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 11:28
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import time, os
from iwebshop.modular import mail

# 指定测试用例目录
test_dir = "./test_case"
catalog = defaultTestLoader.discover(test_dir, pattern="*_test.py")

if __name__ =="__main__":
    case_path = os.path.join(os.getcwd(),"test_case")
    print(case_path)

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义报告存放的位置
    filenames = "./report/" + now + "_result.html"
    fp = open(filenames, "wb")

    # 定义测试报告
    runner = HTMLTestRunner(stream = fp,
                            title="测试报告",
                            description="测试地址 http://192.168.112.132:8888/iwebshop/",
                            tester="xx")
    runner.run(catalog)
    fp.close()
    #mail.senmail()