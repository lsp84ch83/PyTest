# +9+ coding:utf-8 _*_

from tkinter import *

OPTIONS =[
    "California",
    "458",
    "FF",
    "ENZO",
    "LaFerrari"
]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
# *作为形参的时候是起到”打包“的作用；表示调用可变参数函数
# *作为实参的时候是起到“解包”的作用；表示通过解包参数调用函数
w.pack()

mainloop()