# 绘图组件-多边形
from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

center_x = 100
center_y = 50
r = 50 # 半径

points = [
    # 左上角
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 右上角
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 左下角
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    # 定点
    center_x,
    center_y - r,
    # 右下角
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
]

w.create_polygon(points, outline='green', fill='yellow')
# outline外围轮廓线

mainloop()
