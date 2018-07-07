#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : messagebox.py
@version : 
@Time    : 2017/10/31/0031 22:48
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *
import tkinter.messagebox

tkinter.messagebox.askokcancel("Fish Demo", "发射核弹？")
# 格式： askokcancel(title, message, options)
#       title：设置标题栏的文本
#       message：设置对话框的主要文本内容，可以用'\n' 来实现换行
#       options：设置的选项和含义如下表所示
'''
default：1.设置默认的按钮
         2.默认是第一个按钮
         3.可以设置的值根据对话框函数的不同可以选择：CANCEL， IGNORE， OK， NO， RETRY， YES
icon：1.指定对话框显示的图标
      2.可以指定的值有：ERROR, INFO, QUESTION, WARNING
      3.不能指定自己的图标
parent：1.如果不指定该选项，那么对话框默认显示在根窗口上
        2.如果想要将对话框显示在子窗口W上，那么可以设置 parent=W
'''


mainloop()
