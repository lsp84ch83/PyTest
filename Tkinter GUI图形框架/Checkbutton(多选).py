from tkinter import *

root = Tk() # 将Tk()赋值给root

Girls = ['西施','貂蝉','杨玉环','王昭君']

v = []

for girl in Girls:
    v.append(IntVar())
    b = Checkbutton(root, text = girl, variable = v[-1])
    b.pack(anchor = W)  # anchor设置位置
 
mainloop()
