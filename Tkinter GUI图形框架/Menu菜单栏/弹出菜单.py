# _*_ conding:utf-8 _*_

from tkinter import *

root = Tk()
def callback():
    print('你好')
menubar = Menu(root, tearoff=False)
menubar.add_command(label='撤销', command=callback)
menubar.add_command(label='退出', command=root.quit)

frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)

frame.bind("<Button-3>", popup)

mainloop()