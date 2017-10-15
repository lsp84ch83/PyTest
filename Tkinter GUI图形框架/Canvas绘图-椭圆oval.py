# 绘图组件-圆形
from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

w.create_rectangle(40, 20, 160, 80, dash=(4, 4)) # 创建一个矩形
w.create_oval(40, 20, 160, 80, fill='pink') # 创建一个椭圆形 oval
w.create_text(100, 50, text='FishC')

mainloop()
