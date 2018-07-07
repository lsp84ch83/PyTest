# _*_ coding:utf-8 _*_
'''
PanedWindow组件是一个空间管理组件，跟Frame组件类似，
都是为组件提供一个框架，不过PanedWindow允许让用户调整应用城的空间划分
'''
from tkinter import *

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

mainloop()