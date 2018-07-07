# _*_ coding:utf-8 _*_
from tkinter import *

root = Tk()

group = LabelFrame(root, text = '最好的脚本语言是：', padx = 5, pady = 5)
group.pack(padx = 10, pady = 10)

Lange = [
    ('Python',1),
    ('Per',2),
    ('Ruby',3),
    ('Lua',5)]

v = IntVar()
 

for lange,num in Lange:
    b = Radiobutton(group, text = lange, variable = v, value = num, indicatoron = False)
    # indicatoron 设置单选框的形式，False为不显示，True为小圆点显示
    b.pack(fill = X) # fill 设置填充形式，X为横向填充，Y为纵向填充

mainloop()
