# -*- coding:utf-8 -*-
'''
Toplevel(顶级窗口)组件类似于Frame组件；
但Toplevel组件是一个独立的顶级窗口，这种窗口通常拥有标题栏、边框等部件
'''
from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.title("FishC Demo")

    msg = Message(top, text="I Love FishC.com")
    msg.pack()

Button(root, text="创建顶级窗口", command=create).pack()

mainloop()