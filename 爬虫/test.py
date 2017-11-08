#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version : 
@Time    : 2017/11/7/0007 23:27
@license : Copyright(C), Your Company 
'''
from tkinter import *

root = Tk()
w1 = Frame(height=200, width=500)
w2 = Frame(height=50, width=500)
w3 = Frame(height=30, width=500)
w1.grid_propagate(0)
w2.grid_propagate(0)
w1.grid(row=0, column=0, padx=2, pady=5)
w2.grid(row=1, column=0, padx=2, pady=5)
w3.grid(row=2, column=0)
t1 = Text(w1)
t2 = Text(w2)
send_button = Button(w3, text="发送")
file_button = Button(w3, text="发送文件")

t1.grid()
t2.grid()
send_button.grid(sticky=W)
Label(w3, text=" " * 90).grid(row=0, column=1)
file_button.grid(row=0, column=2, sticky=E)
root.mainloop()