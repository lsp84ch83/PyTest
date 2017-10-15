# 判断鼠标状态，从而打开预定网页
from tkinter import *
import webbrowser

root = Tk()

text1 = Text(root, width = 30, height = 5)
text1.pack()

text1.insert(INSERT, 'I Love Fishc.com!')

text1.tag_add('link', '1.7', '1.16')
text1.tag_config('link', foreground = 'blue', underline = True)

def show_arrow_cursor(event):
    text1.config(cursor = 'arrow')
    # 设置鼠标cursor状态

def show_xterm_cursor(event):
    text1.config(cursor = 'xterm')

def click(event):
    webbrowser.open('https://www.baidu.com')

text1.tag_bind('link', '<Enter>', show_arrow_cursor)
text1.tag_bind('link', '<Leave>', show_xterm_cursor)
text1.tag_bind('link', '<Button>', click)


mainloop()
