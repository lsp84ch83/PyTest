#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
@Author  : Soner
@File    : filedialog文件对话框.py
@version : 
@Time    : 2017/10/31/0031 23:13
@Software: PyCharm
@Contact : 317152347@QQ.com
@license : Copyright(C), Your Company 
'''
from tkinter import *
import tkinter.filedialog

root = Tk()

def callback():
    fileName = tkinter.filedialog.askopenfilename()
    print(fileName)
'''
filedialog 模块提供了两个函数：askopenfilename() 和 asksaveasfilename(),分别用于打开文件和保存文件

两个函数可供设置的选项是一样的：
defaultextension：1.指定文件的后缀
                  2.例如：defaultextension=".jpg"，那么当用户输入一个文件名“Fishc”的时候，文件名汇自动添加后缀为“Fishc.jpg”
                  3.如果用户输入文件名包含后缀，那么该选项不生效
filetypes：1.指定筛选文件类型的下拉菜单选项
           2.该选项的值是由 2 元祖构成的列表
           3.每个 2 元祖有（类型名，后缀）构成。例如：filetypes=[("PNG", ".png"),("JPG", ".jpg"),("GIF"， “.gif”)]
initialdir：1.指定打开/保存文件的默认路径
            2.默认路径是当前文件夹
parent：1.如果不指定该选项，那么对话框默认显示在根窗口上
        2.如果想要将对话框显示在子窗口W上，那么可以设置parent=W
title：1.指定文件对话框的标题栏文本
'''

Button(root, text="打开文件", command=callback).pack()

mainloop()