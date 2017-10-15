from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode = EXTENDED)
'''selectmode 设置选择方式：
    SINGLE(单选)
    BROWSE(单选，拖动鼠标或通过方向键可以直接改变选项)
    MULTIPLE(多选)
    EXTENDED(多选，可以使用SHIFT或者Ctrl键实现)
    默认是BROWSE
    '''
theLB.pack()

for item in ['鸡蛋','鸭蛋','鹅蛋','狗蛋']:
    theLB.insert(END,item)



mainloop()
