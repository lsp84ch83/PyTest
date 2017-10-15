# 文本搜索
from tkinter import *
import hashlib

root = Tk()

text1 = Text(root, width = 30, height = 5)
text1.pack()

text1.insert(INSERT, 'I Love Fishc.com!') # 插入一个文本内容

def getIndex(text1, index):
    # 转换为行列格式的元组
    return tuple(map(int,str.split(text1.index(index), '.')))

start = '1.0' # 起始位置
while True:
    pos = text1.search('o', start, stopindex = END)
    # 搜索的范围 start 开始位置； stopindex 结束位置
    if not pos:
        break
    print("找到了，位置是：", getIndex(text1, pos))
    start = pos + '+1c'
    # 指向下一个字符


mainloop()
