#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/12 20:53
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from tkinter import *
from tkinter import messagebox

def closeWindow():
    messagebox.showinfo(title="警告", message="不许关闭，好好回答")
    return

def Love():
    # 顶级窗口
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title("好巧，我也是")
    label = Label(love,text="好巧，我也是", font = ("微软雅黑", 20))
    label.pack()
    label = Label(love,text="加个微信呗~~", font = ("微软雅黑", 20))
    label.pack()

    label1 =  Entry(love, font = ("微软雅黑", 14))
    label1.pack()

    btn = Button(love, text = "确定", width = 10, height = 2, command = closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)


def closelove():
    return

# 关闭所有窗口库
def closeallwindow():
    # 销毁
    window.destroy()

def noLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+260")
    no_love.title("在考虑考虑")
    label = Label(no_love, text = "再考虑考虑", font = ("微软雅黑",25))
    label.pack()

    btn = Button(no_love, text = "好的", width = 10, height = 2, command = no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closenolove)

def closenolove():
    messagebox.showinfo("在考虑一下","在考虑一下")

# 创建窗口
window = Tk()
# 窗口标题
window.title("你喜欢我吗？")
# 窗口大小
window.geometry("380x420+500+240")
# 窗口位置
# window.geometry("+500+240")
# protocol 用户关闭窗口出发的事件
window.protocol("WM_DELETE_WINDOW", closeWindow)


# 标签控件
label = Label(window, text='hey,小姐姐',font=("微软雅黑",15),fg="red")
# 定位
label.grid(row = 0, column = 0)

label1 = Label(window, text='喜欢我吗？',font=("微软雅黑",15),fg="red")

# sticky 对齐方式 N S W E
label1.grid(row = 1, column = 1, sticky = E)

# 显示图片
photo = PhotoImage(file="./兔子.png")
imageLable = Label(window, image = photo)
# columnspan 组件所跨越的列数
imageLable.grid(row = 2, columnspan = 2)

# 按钮控件
# command 点击触发的事件
btn = Button(window, text="喜欢", width=15, height=2, command=Love)
btn.grid(row = 3, column=0, sticky=W)

btn1 = Button(window, text="不喜欢", command = noLove)
btn1.grid(row = 3, column=1, sticky=E)


# 显示窗口 消息循环
window.mainloop()
