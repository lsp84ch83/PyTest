# 验证文本是否发生改变
from tkinter import *
import hashlib

root = Tk()

text1 = Text(root, width = 30, height = 5)
text1.pack()

text1.insert(INSERT, 'I Love Fishc.com!')
contents = text1.get('1.0', END) # 获取文本内容

def getSig(contents):
    m = hashlib.md5(contents.encode()) # 获取文本的MD5值
    return m.digest()

sig = getSig(contents)

def check():
    contents = text1.get('1.0', END)
    if sig != getSig(contents): # 对比文本的MD5值
        print('内容发生改变')
    else:
        print('无内容改变')

Button(root, text = '检查', command = check).pack()


mainloop()
