#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : Place指定组件的大小和位置.py
@version : 
@Time    : 2017/10/26/0026 22:38
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *

root = Tk()
'''
def callback():
    print("Bigo")
Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)
# anchor=CENTER 居中显示
'''
# 父组件相对高宽
Label(root, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
Label(root, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
Label(root, bg="green").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)
# 父组件相对高度百分比:relheight
# 父组件相对宽度百分比:relwidth

mainloop()