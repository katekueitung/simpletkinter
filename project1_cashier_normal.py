
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image

# what could do more:
# 1. add "buy x get y free"
# 2. perhaps add '+','-' icon for goods quantity

def event1():

    global entry1
    global entry2
    global v1
    global v2
    global v3

    t1 = entry1.get()
    print("綿綿冰數量：",t1,"杯",int(float(t1)*45),"元")

    t2 = entry2.get()
    print("刨冰數量:",t2,"碗",int(float(t2)*50),"元")
    print("合計：",int(float(t1)*45)+int(float(t2)*50),"元")
    # ### Step4: now we can show the entry after pressing a button
    v1.set(int(float(t1)*45))
    v2.set(int(float(t2)*50))
    v3.set(int(float(t1)*45)+int(float(t2)*50))

win = tk.Tk()

win.wm_title("笛園綿綿冰城 POS System")
win.minsize(width=800, height=1000)
win.maxsize(width=800, height=1000)
win.resizable(width=False, height=False)

background_image= ImageTk.PhotoImage(Image.open("menu background.jpg"))
background_label= tk.Label(win, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

labeltitle =tk.Label(win,text="歡迎來到笛園綿綿冰城!",bg="white",fg="blue",font=("",20))
labeltitle.place(x=250, y=110)

v1 = StringVar()
label1 =tk.Label(win, text = "hahaha",textvariable=v1)

#
v2 =StringVar()
label2 =tk.Label(win, text = "hahaha",textvariable=v2)

v3 =StringVar()
label3 =tk.Label(win, text = "hahaha",textvariable=v3)
label3.place(x=375,y=460)
v3.set("...")

img1 = ImageTk.PhotoImage(Image.open("ice1.jpg"))
btn1 =tk.Button(win,text="綿綿冰",image=img1,command=event1)
btn1.place(x=180,y=150)

Label1 =tk.Label(win,text="綿綿冰每杯 45元")
Label1.place(x=245,y=380)  ### resize font


img2 = ImageTk.PhotoImage(Image.open("ice2.jpg"))
btn2 =tk.Button(win,text="綿綿冰",image=img2,command=event1)
btn2.place(x=400,y=150)


Label2 =tk.Label(win,text="刨冰每碗 50元")
Label2.place(x=475,y=380)

entry1=tk.Entry(win,width=5)
entry1.place(x=250,y=330)


entry2=tk.Entry(win,width=5)
entry2.place(x=480,y=330)


btn3=tk.Button(win,text="合計",command=event1)
btn3.place(x=335,y=461)

labelcur =tk.Label(win,text="元")
labelcur.place(x=405, y=460)
labeltitle =tk.Label(win,text="餐點均為現做，感謝您的耐心等候!",bg="white",fg="blue",font=("",20))
labeltitle.place(x=220, y=560)

win.mainloop()