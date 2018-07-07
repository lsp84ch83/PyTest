# _*_ conding:utf-8 _*_

from tkinter import *

root = Tk()
def callback():
    print('你好')

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False)
# tearoff的属性，改变创建的菜单是否新打开窗口显示;
# 默认是True，新窗口显示；False为本窗口打开
filemenu.add_command(label='打开', command=callback)
filemenu.add_command(label='保存', command=callback)
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='剪切', command=callback)
editmenu.add_command(label='拷贝', command=callback)
editmenu.add_command(label='黏贴', command=callback)
menubar.add_cascade(label='编辑', menu=editmenu)

root.config(menu=menubar)

mainloop()