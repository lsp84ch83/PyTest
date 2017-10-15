# 文本的撤销操作
from tkinter import *
import hashlib

root = Tk()

text = Text(root,width=30, height=5, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT,'I Love Fishc.com!')

def callback(event):
    text.edit_separator()
    # 插入一个分隔符

text.bind('<Key>', callback) # 绑定键盘事件


def show():
    text.edit_undo()
    # 调用Undo撤销功能，默认为关闭，需要undo=True打开

Button(root, text='撤销', command=show).pack()

mainloop()
