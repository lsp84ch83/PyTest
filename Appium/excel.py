#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 14:36
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company
import xlrd,xlwt,xlutils


#  打开 EXCEL表
wb = xlrd.open_workbook('F:\PyTest\Appium\data.xls')
#  获取Excel表Sheet页
sh = wb.sheet_by_name('note')
#  获取Excel数据 cell_value(i, j) 获取i 行，j 列
user1 = sh.cell_value(0, 0)

print(user1)

