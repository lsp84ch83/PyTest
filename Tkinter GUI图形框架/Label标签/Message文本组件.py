# _*_ coding:utf-8 _*_
'''
Message 是Label组件的变体，用于显示多行文本消息；
Message组件能够自动换行，并调整文本的尺寸使其适应给定的尺寸
'''
from tkinter import *

root = Tk()

w1 = Message(root, text="这是一则消息", width=100)
w1.pack()

w2 = Message(root, text="这是一则骇人听闻的非常难得一见的很长的消息", width=100)
w2.pack()


mainloop()