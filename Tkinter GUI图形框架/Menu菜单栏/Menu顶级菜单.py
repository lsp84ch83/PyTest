# -*- conding:utf-8 -*-

from tkinter import *

root = Tk()
def callback():
    print('你好')
menubar = Menu(root)
menubar.add_command(label='帮助', command=callback)
menubar.add_command(label='退出', command=root.quit)

root.config(menu=menubar)

mainloop()