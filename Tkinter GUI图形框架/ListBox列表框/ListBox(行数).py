from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode = EXTENDED,height = 10)
# height 可以设置列表显示的行数；列表默认显示10行

theLB.pack()

for item in range(15):
    theLB.insert(END,item)



mainloop()
