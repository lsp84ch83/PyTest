
'''
a=float(input(""))

b=a/6.6147

c=a/7.8445

print("ת��Ϊ��Ԫ:{:.2f}".format(b))

print("ת��ΪŷԪ:{:.2f}".format(c))
'''

'''
# _*_ coding:utf-8 _*_
val = input('��������¶ȱ�ʶ���õ��¶�ֵ�����磺32C����')
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print('ת����ĵ��¶�Ϊ��%.2fF' % f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.6
    print('ת������¶�Ϊ��%.2fC' % c)
else:
    print('��������')
'''

'''
# tkinter ��һ������
import tkinter as tk

app = tk.Tk()
app.title('FichsS Demo')

theLabel = tk.Label(app, text='��һ������')
theLabel.pack()

app.mainloop()
'''

'''
from tkinter import *

root = Tk()

photo = PhotoImage(file = 'bg.gif')
theLabel = Label(root,
                 text = 'ѧPython\n�� FishC',
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font = ('΢���ź�',20),
                 fg = 'white'
                 )
theLabel.pack()

 
mainloop()
'''


from random import randint

name=raw_input('���')

f=open('game.txt')
lines=f.readlines()
f.close()
