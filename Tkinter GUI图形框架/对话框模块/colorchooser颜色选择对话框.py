#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@File    : colorchooser颜色选择对话框.py
@version : 
@Time    : 2017/10/31/0031 23:31
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *
import tkinter.colorchooser

root = Tk()

def callback():
    fileName = tkinter.colorchooser.askcolor()
    print(fileName)

'''


'''

Button(root, text="选择颜色", command=callback).pack()

mainloop()
