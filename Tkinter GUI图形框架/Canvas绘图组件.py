# 绘图组件-画布
from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

w.create_line(0, 50, 200, 50, fill='yellow') #创建一条横线
w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4)) # 创建一条竖线
w.create_rectangle(50, 25, 150, 75, fill='blue') # 创建一个矩形




mainloop()
