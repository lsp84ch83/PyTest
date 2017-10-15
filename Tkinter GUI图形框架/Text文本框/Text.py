from tkinter import *

root = Tk()

text1 = Text(root, width = 80, height = 49)
text1.pack() 

photo = PhotoImage(file = 'bg.gif')

def show():
    text1.image_create(END, image = photo)

b1 = Button(text1, text = '点我', command = show)
text1.window_create(INSERT, window = b1)

mainloop()
