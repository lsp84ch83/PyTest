#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version : 
@Time    : 2017/11/7/0007 21:35
@license : Copyright(C), Your Company 
'''
import urllib.request
import urllib.parse
import json
import time
from tkinter import *



def translation():
    content=text1.get(1.0,END)
    if content=='':
        content="简约——寻找生活中最绚丽的一幕"
    url='http://fanyi.baidu.com/v2transapi'

    data = {}
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['query'] = content
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0')

    response=urllib.request.urlopen(req,data)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    text2.delete(0.0, END)
    text2.insert(INSERT,target['trans_result']['data'][0]['dst'])

def qc():
    text1.delete(0.0, END)
    text2.delete(0.0, END)

root = Tk()
label=Label(root, text="Sometimes中英文翻译软件V1.0",fg="blue",font=("黑体", 13, "bold"))
text1=Text(root, width=50, height=12, padx=10, pady=10, font=("黑体", 13, "bold"))
text2=Text(root, width=50, height=12, padx=10, pady=10, font=("黑体", 13, "bold"))
#text2.insert(INSERT,"请再上面的文本框输入您想翻译的文字")
button1=Button(text="开始翻译", width=10, fg="black", bg="#5ac", command=translation)
button2=Button(text="清除", width=10, fg="black", bg="#5ac", command=qc)
label.pack()
text1.pack()
text2.pack()
button1.pack(side=LEFT, padx=50, pady=5)
button2.pack(side=RIGHT, padx=50, pady=5)

mainloop()
