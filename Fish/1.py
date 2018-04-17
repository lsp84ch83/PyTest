
'''
a=float(input(""))

b=a/6.6147

c=a/7.8445

print("转换为美元:{:.2f}".format(b))

print("转换为欧元:{:.2f}".format(c))
'''

'''
# -*- coding:utf-8 -*-
val = input('请输入带温度标识符好的温度值（例如：32C）：')
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print('转换后的的温度为：%.2fF' % f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.6
    print('转换后的温度为：%.2fC' % c)
else:
    print('输入有误')
'''

'''
# tkinter 第一个窗口
import tkinter as tk

app = tk.Tk()
app.title('FichsS Demo')

theLabel = tk.Label(app, text='第一个窗口')
theLabel.pack()

app.mainloop()
'''

'''
from tkinter import *

root = Tk()

photo = PhotoImage(file = 'bg.gif')
theLabel = Label(root,
                 text = '学Python\n到 FishC',
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font = ('微软雅黑',20),
                 fg = 'white'
                 )
theLabel.pack()

 
mainloop()
'''


from random import randint

name=raw_input('你好')

f=open('game.txt')
lines=f.readlines()
f.close()
