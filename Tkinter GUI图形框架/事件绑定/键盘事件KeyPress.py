# _*_ coding:utf-8 _*_

from tkinter import *

root = Tk()

def callback(event):
    print(event.char)
    # char 获取当前的字符

frame = Frame(root, width=200, height=200)
frame.bind("<Key>", callback)
frame.focus_set()
# 获得焦点
frame.pack()

mainloop()