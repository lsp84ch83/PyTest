#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : Pack按添加顺序排列组件.py
@version : 
@Time    : 2017/10/26/0026 22:38
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *

root = Tk()

'''
纵向填充
Label(root, text="red", bg="red", fg="white").pack(fill=X)
Label(root, text="green", bg="green", fg="black").pack(fill=X)
Label(root, text="blue", bg="blue", fg="white").pack(fill=X)
'''
# 横向填充
Label(root, text="red", bg="red", fg="white").pack(side=LEFT)
Label(root, text="green", bg="green", fg="black").pack(side=LEFT)
Label(root, text="blue", bg="blue", fg="white").pack(side=LEFT)

mainloop()