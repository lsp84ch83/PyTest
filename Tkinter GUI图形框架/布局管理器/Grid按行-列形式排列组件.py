#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : Grid按行-列形式排列组件.py
@version : 
@Time    : 2017/10/26/0026 22:38
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *

root = Tk()

Label(root, text="用户名").grid(row=0, sticky = W)
Label(root, text="密码").grid(row=1, sticky = W)

photo = PhotoImage(file="8.gif")
Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx=5, pady=5)

Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

Button(root, text="确认", width=10).grid(row=3, columnspan=3, pady=5)
# sticky是设置 字体对齐方式
mainloop()