# -*- coding:utf-8 -*-
'''
Spinbox组件是Entry组件的变体，用于从一些固定的值中选取一个
'''
from tkinter import *

root = Tk()

#w = Spinbox(root, from_=0, to=10)
w = Spinbox(root, values=("熊大", "熊二", "光头强","国王"))
w.pack()

mainloop()