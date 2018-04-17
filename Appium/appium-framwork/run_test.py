#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 16:25
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import sys

reload(sys)  # 加载
sys.setdaultencoding('utf-8')

'''
驱动程序：运行思路
1> 获取框架脚本位置
2> 选取需要运行的脚本，加载到测试集
3> 测试报告设计
4> 发送邮件设置
5> 运行脚本
'''
# 1> 获取框架脚本位置
# 2> 选取需要运行的脚本，加载到测试集
# 3> createSuite() 创建测试集的函数

def createSuite():
