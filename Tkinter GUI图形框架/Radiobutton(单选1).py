from tkinter import *

root = Tk()

Lange = [
    ('Python',1),
    ('Per',2),
    ('Ruby',3),
    ('Lua',5)]

v = IntVar()
v.set(1)

for lange,num in Lange:
    b = Radiobutton(root, text = lange, variable = v, value = num, indicatoron = False)
    # indicatoron 设置单选框的形式，False为不显示，True为小圆点显示
    b.pack(fill = X) # fill 设置填充形式，X为横向填充，Y为纵向填充

mainloop()
