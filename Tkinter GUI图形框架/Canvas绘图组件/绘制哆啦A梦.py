from tkinter import *
root = Tk()

#画板
w = Canvas(root,width=600,heigh=600,background="white")
w.pack()

#头
w.create_oval(180,100,420,340,outline="black",fill="#1E90FF")
#脸
w.create_oval(200,140,400,340,outline="black",fill="white")

#眼睛
w.create_oval(250,120,300,180,outline="black",fill="white")
w.create_oval(300,120,350,180,outline="black",fill="white")
w.create_oval(280,140,295,160,outline="black",fill="black")
w.create_oval(305,140,320,160,outline="black",fill="black")
w.create_oval(285,145,290,155,outline="black",fill="white")
w.create_oval(310,145,315,155,outline="black",fill="white")

#鼻子
w.create_oval(290,165,310,185,outline="black",fill="red")
w.create_line(300,185,300,270,fill="black")

#嘴巴
w.create_arc(230,180,370,270,style="arc",start=215,extent=110,fill="black")

#胡子
w.create_line(230,185,280,200,fill="black")
w.create_line(220,215,280,215,fill="black")
w.create_line(230,245,280,230,fill="black")
w.create_line(370,185,320,200,fill="black")
w.create_line(380,215,320,215,fill="black")
w.create_line(370,245,320,230,fill="black")

# 身体
w.create_rectangle(210,300,390,450,fill="#1E90FF")

#肚子
w.create_oval(230,280,370,420,outline="black",fill="white")
w.create_arc(250,280,350,320,style="pieslice",start=0,extent=180,\
             outline="white",fill="white")

#项圈
w.create_line(210,300,390,300,capstyle="round",width=15,fill="red")

#铃铛
w.create_oval(285,300,315,330,outline="black",fill="yellow")
w.create_rectangle(285,310,315,315,outline="black",fill="yellow")
w.create_oval(296,318,304,326,outline="black",fill="red")
w.create_line(300,326,300,330,fill="black")

#口袋
w.create_arc(250,300,350,400,style="pieslice",start=180,extent=180,\
             outline="black",fill="white")

#脚
w.create_arc(280,430,320,470,style="pieslice",start=0,extent=180,\
             outline="black",fill="white")
w.create_line(280,450,320,450,fill="white")
w.create_oval(190,430,290,470,outline="black",fill="white")
w.create_oval(410,430,310,470,outline="black",fill="white")

#手
points_1=[210,310,170,350,190,370,210,360]
w.create_polygon(points_1,outline="black",fill="#1E90FF")
w.create_oval(150,346,190,386,outline="black",fill="white")
points_2=[390,310,430,350,410,370,390,360]
w.create_polygon(points_2,outline="black",fill="#1E90FF")
w.create_oval(450,346,410,386,outline="black",fill="white")
w.create_line(210,310,210,350,fill="#1E90FF")
w.create_line(390,310,390,350,fill="#1E90FF")

mainloop()
