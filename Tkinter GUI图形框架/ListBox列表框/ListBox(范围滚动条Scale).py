from tkinter import *

root  = Tk()

s1 = Scale(from_ = 0, to = 42, tickinterval = 15, length = 200, resolution = 1)
s1.pack(side = RIGHT)
'''
1. orient 设置 水平或垂直 位置
2. length 设置 像素大小
3. tickinterval 设置 显示刻度的步长
4. resolution 设置 滚动条间隔步长
'''

s2 = Scale(from_ = 0, to = 200, resolution = 10, length = 600, orient = HORIZONTAL)
s2.pack(side = BOTTOM)

def show():
    print(s1.get(), s2.get())

Button(root, text = '获取位置', command = show).pack()

mainloop()
