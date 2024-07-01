import tkinter
import time
import random
"""
a = tkinter.Tk()
a.title("Dima")
a.geometry("500x500+1000+100")
a.resizable(False,False)
a.minsize(300,300)
a.maxsize(700,700)
photo=tkinter.PhotoImage(file="C:/Users/Python/pythonProject5/photo.png")
a.iconphoto(False,photo)
a.config(bg="#E96FE9")
label_1 = tkinter.Label(a, text="дарова",
                        bg="#E96FE9",
                        font = ("Times Nev Roman",20,"bold"),
                        padx = 150,
                        pady = 200,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20)
a.mainloop()
label_1.pack()
"""
"""
b = tkinter.Tk()
b.title(".")
b.geometry("1600x840+0+0")
b.config(bg="#fffb00")







label_1 = tkinter.Label(b, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=20,
                        height=7,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        )
label_1.place(x=150,y=10)

label_2 = tkinter.Label(b, text="привет",
                        bg="#f26805",
                        font = ("Times Nev Roman",20,"bold"),
                        padx = 100,
                        pady = 50,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 5)
label_2.place(x=200,y=500)

label_3 = tkinter.Label(b, text="привет",
                        bg="#875ec2",
                        width=20,
                        height=10,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 10)
label_3.place(x=500,y=300)


label_4 = tkinter.Label(b, text="привет",
                        bg="#09e075",
                        font = ("Times Nev Roman",20,"bold"),
                        width = 30,
                        height = 10,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 15)
label_4.place(x=800,y=100)

label_5 = tkinter.Label(b, text="привет",
                        bg="#a10d0d",
                        font = ("Times Nev Roman",20,"bold"),
                        width=25,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 25)
label_5.place(x=900,y=500)
b.mainloop()
"""

"""
btn.place(x=100,y=200)
def hello():

    print("hello")
win.mainloop()
"""
"""
i=0
n=0
l=0
o=0
p=0
def hello():
    global i
    a = ["wwgfdvsd", 'dsfdsdfv', '1243']
    label_1['text'] = a[i]
    i += 1
    if i>=3:
        i = 0

    global n
    v = ["red","#f26805","#a10d0d"]
    label_2["bg"] = v[n]
    n += 1
    if n>=3:
        n = 0
    global l
    r = ["5","10","20"]
    label_3["width"] = r[l]
    l += 1
    if l>=3:
        l = 0
    global o
    f = ["7", "15", "30"]
    label_4["bd"] = f[o]
    o += 1
    if o>=3:
        o = 0
    global p
    f = ["s", "w", "e"]
    label_5["anchor"] = f[p]
    p += 1
    if p >= 3:
        p = 0
win = tkinter.Tk()
win.geometry("1980x1080")
win.config(bg="#fffb00")
label_1 = tkinter.Label(win, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=10,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20,
                        )

btn = tkinter.Button(win, text = "кнопка",
                     command=hello,
                     cursor="spider",
                     )

label_2 = tkinter.Label(win, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=10,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20,
                        )
label_3 = tkinter.Label(win, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=10,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20,
                        )
label_4 = tkinter.Label(win, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=10,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20,
                        )
label_5 = tkinter.Label(win, text="привет",
                        bg="#ff0000",
                        font = ("Times Nev Roman",20,"bold"),
                        width=10,
                        height=5,
                        anchor="sw",
                        relief=tkinter.RAISED,
                        bd = 20,
                        )
label_1.place(x=1000,y=200)
label_2.place(x=500,y=100)
label_3.place(x=300,y=500)
label_4.place(x=70,y=400)
label_5.place(x=700,y=350)
btn.place(x=200,y=200)


win.mainloop()

label_1
"""
"""
def hello ():
    a = emt.get()
    lbl1["text"]=a



def delt():
    emt.delete(0,"end")
def deight():
    emt.insert("end","gwe")


win = tkinter.Tk()
win.geometry("900x600")
win.config(bg="#09a1d4")



emt = tkinter.Entry(win,font=("times new roman",40,"bold"),
                              show="#")
emt.pack()
btn = tkinter.Button(win,text="принять",
                     command=hello).pack()
btn1 = tkinter.Button(win,text="удалить",
                     command=delt).pack()
lbl1 = (tkinter.Label(win,text="gwe",
              width=20,
              height=10))
lbl1.place(x=400,y=200)


win.mainloop()
"""
"""
def hello ():
    a = emt.get()#окно вода логина
    b = emt1.get()#окно вода пароля
    global login
    global poroll
    if a == login and b == poroll :
        print("вы вошли в акаунт")
    else:
        print("неверный логин или пароль")
    v = btn1.get()
    if v !=login and v != poroll:
        print("вы создали новый акаунт")



def delt():
    emt.delete(0,"end")
def deight():
    emt.insert("end","gwe")




login = "qwe"
poroll = "123"

win = tkinter.Tk()
win.geometry("900x600")
win.config(bg="#09a1d4")

emt = tkinter.Entry(win,font=("times new roman",15,"bold"),
                              show="",
                              bg = "#09a1d4",
                              )
emt.place(x=500,y=200)

emt1 = tkinter.Entry(win,font=("times new roman",15,"bold"),
                              show="#",
                              bg = "#09a1d4",
                              )
emt1.place(x=500,y=250)

btn = tkinter.Button(win,text="войти",
                     command=hello,
                     width=5,
                     height=2,
                     )

btn1 = tkinter.Button(win,text="зарегестрироватся",
                     command=hello,
                      width=40,
                      height=2)
label_1 = tkinter.Label(win, text="ведите электронную почту",
                        bg="#09a1d4",
                        font = ("Times Nev Roman",),
                        width=25,
                        height=1,
                        relief=tkinter.RAISED,
                        )
label_2 = tkinter.Label(win, text="ведите пароль",
                        bg="#09a1d4",
                        font = ("Times Nev Roman",),
                        width=25,
                        height=1,
                        relief=tkinter.RAISED,
                        cursor="man",
                        )
label_1.place(x=150,y=200)
label_2.place(x=150,y=250)
btn.place(x=300,y=350)
btn1.place(x=350,y=350)




win.mainloop()
"""
""" 
t= True
while t:
    try:
        s = input()
        file = open(s,'r')
        t=False
        print("такой файл есть")
        if s == "exzit":
            t=False


    except FileNotFoundError:
        print("такого файла нет,попробуйте ещё")

"""
"""
fonntext = ("Times Nev Roman",27,"bold")
def locate():
    vvodTxt.place(x=10,y=10)
    btnsprt.place(x=210,y=60)
    btnRas.place(x=110,y=60)
    btnUmn.place(x=10,y=60)
    btn1.place(x=10,y=350)
    btn2.place(x=110,y=350)
    btn3.place(x=210, y=350)
    btn4.place(x=10, y=250)
    btn5.place(x=110, y=250)
    btn6.place(x=210, y=250)
    btn7.place(x=10, y=150)
    btn8.place(x=110, y=150)
    btn9.place(x=210, y=150)
    btn0.place(x=110, y=450)
    btna.place(x=300, y=250)
    btnb.place(x=300, y=350)
    btnc.place(x=300, y=450)
    btnf.place(x=210, y=450)
    btng.place(x=300, y=150)
    btns.place(x=10, y=450)
    btnh.place(x=300, y=60)
def qwe():
    a = vvodTxt.get().split("=")
    if len(a)>1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])
def bt1():
    vvodTxt.insert(tkinter.END,"1")
def btUmn():
    vvodTxt.insert(tkinter.END,"*")
    qwe()
def bt2():
    vvodTxt.insert(tkinter.END,"2")
def bt3():
    vvodTxt.insert(tkinter.END,"3")
def bt4():
    vvodTxt.insert(tkinter.END, "4")
def bt5():
    vvodTxt.insert(tkinter.END,"5")
def bt6():
    vvodTxt.insert(tkinter.END,"6")
def bt7():
    vvodTxt.insert(tkinter.END,"7")
def bt8():
    vvodTxt.insert(tkinter.END,"8")
def bt9():
    vvodTxt.insert(tkinter.END,"9")
def bt0():
    vvodTxt.insert(tkinter.END,"0")
def btsprt():
    s = float(vvodTxt.get())
    res = math.sqrt(s)
    vvodTxt.delete(0,tkinter.END)
    vvodTxt.insert(tkinter.END, res)
def btRas():
    vvodTxt.insert(tkinter.END,"/")
    qwe()
def bta():
    vvodTxt.insert(tkinter.END,"+")
    qwe()
def btb():
    vvodTxt.insert(tkinter.END,"-")
    qwe()
def btc():
    try:
        a=vvodTxt.get()
        res = eval(a)
        result = "="+str(res)

        vvodTxt.insert(tkinter.END,result)
    except SyntaxError:
        pass
def btf():
    vvodTxt.insert(tkinter.END,".")
def btg():
    vvodTxt.insert(tkinter.END, "**")
def bts():
    vvodTxt.delete(0,tkinter.END)
def bth():
    a= str(len(vvodTxt.get())-1)
    vvodTxt.delete(a)
calc = tkinter.Tk()
calc.config(bg="#006666")
calc.geometry("400x550+640+150")
calc.title("калькулятор")
vvodTxt=tkinter.Entry(calc,font=fonntext)
btnsprt= tkinter.Button(calc,text=" √",font=fonntext,
                           pady=4,
                           padx=5,
                           command=btsprt)

btnRas = tkinter.Button(calc,text="/",font=fonntext,
                            pady=4,
                            padx=15,
                            command=btRas)

btnUmn = tkinter.Button(calc,text="*",font=fonntext,
                           pady=4,
                           padx=12,
                           command=btUmn
                           )
                         command=bt1)
                         padx=10,
                         command=bt2)

btn3 = tkinter.Button(calc,text="3",font=fonntext,
                         pady=4,

btn1 = tkinter.Button(calc,text="1",font=fonntext,
                         pady=4,
                         padx=10,
                         padx=10,


btn2 = tkinter.Button(calc,text="2",font=fonntext,
                         pady=4,
                         command=bt3)

btn4 = tkinter.Button(calc,text="4",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt4)

btn5 = tkinter.Button(calc,text="5",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt5)

btn6 = tkinter.Button(calc,text="6",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt6)

btn7 = tkinter.Button(calc,text="7",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt7)

btn8 = tkinter.Button(calc,text="8",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt8)

btn9 = tkinter.Button(calc,text="9",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt9)

btn0 = tkinter.Button(calc,text="0",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bt0)

btna = tkinter.Button(calc,text="+",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bta)

btnb = tkinter.Button(calc,text="-",font=fonntext,
                         pady=4,
                         padx=14,
                         command=btb)

btnc = tkinter.Button(calc,text="=",font=fonntext,
                         pady=4,
                         padx=10,
                         comman=btc)

btnf = tkinter.Button(calc,text=".",font=fonntext,
                         pady=4,
                         padx=15,
                         command=btf)

btng = tkinter.Button(calc,text="^",font=fonntext,
                         pady=4,
                         padx=10,
                         command=btg)

btns = tkinter.Button(calc,text="C",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bts)

btnh = tkinter.Button(calc,text="<",font=fonntext,
                         pady=4,
                         padx=10,
                         command=bth)

locate()

def btlvn():
    vvodTxt.insert(tkinter.END,"+")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a)!=1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def btmn():
    vvodTxt.insert(tkinter.END,"*")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def batton():
    vvodTxt.insert(tkinter.END,"/")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def main():
    vvodTxt.insert(tkinter.END,"-")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def hello():
    vvodTxt.insert(tkinter.END,".")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def kakdela():
    vvodTxt.insert(tkinter.END,"<")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def dosvidanie():
    vvodTxt.insert(tkinter.END,"^")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def end():
    vvodTxt.insert(tkinter.END,"C")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

def powvart():
    vvodTxt.insert(tkinter.END,"√")

    a = vvodTxt.get()
    a = a.split("=")
    if len(a) != 1:
        vvodTxt.delete(0,tkinter.END)
        vvodTxt.insert(0,a[1])

    print(enabled.get())
     x_win["text"] = "Игрок x: " + str("pobeda x")
    o_win["text"] = "Игрок 0: " + str("pobeda 0")
    
calc.mainloop()
"""
"""
from tkinter import *
tic = True
a = True
def label_1():
    global tic
    b = [bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9]
    for i in range(0,9):
        b[i]["text"]=""
    print("игра началась заново")

def black():
    if enabled.get() == 1:
        bt9 ["bg"] = "#858477"
        bt8 ["bg"] = "#858477"
        bt7 ["bg"] = "#858477"
        bt6 ["bg"] = "#858477"
        bt5 ["bg"] = "#858477"
        bt4 ["bg"] = "#858477"
        bt3 ["bg"] = "#858477"
        bt2 ["bg"] = "#858477"
        bt1 ["bg"] = "#858477"

        bt9["fg"] = "#858477"
        bt8["fg"] = "#858477"
        bt7["fg"] = "#858477"
        bt6["fg"] = "#858477"
        bt5["fg"] = "#858477"
        bt4["fg"] = "#858477"
        bt3["fg"] = "#858477"
        bt2["fg"] = "#858477"
        bt1["fg"] = "#858477"
    else :
        bt9 ["bg"] = "white"
        bt8 ["bg"] = "white"
        bt7 ["bg"] = "whit"
        bt6 ["bg"] = "white"
        bt5 ["bg"] = "white"
        bt4 ["bg"] = "white"
        bt3 ["bg"] = "white"
        bt2 ["bg"] = "white"
        bt1 ["bg"] = "white"

        bt9["fg"] = "white"
        bt8["fg"] = "white"
        bt7["fg"] = "white"
        bt6["fg"] = "white"
        bt5["fg"] = "white"
        bt4["fg"] = "white"
        bt3["fg"] = "white"
        bt2["fg"] = "white"
        bt1["fg"] = "white"




def b1():
    global tic
    if bt1["text"] == "":
        if tic == True:
            bt1["text"]="X"
            tic  = False
        elif tic == False:
            bt1["text"]="0"
            tic = True
    pobeda()
    winn()
def b2():
    global tic
    if bt2["text"] == "":
        if tic == True:
            bt2["text"]="X"
            tic  = False
        elif tic == False:
            bt2["text"]="0"
            tic = True
    pobeda()
    winn()
def b3():
    global tic
    if bt3["text"]=="":
        if tic == True:
            bt3["text"]="X"
            tic  = False
        elif tic == False:
            bt3["text"]="0"
            tic = True
    pobeda()
    winn()
def b4():
    global tic
    if bt4["text"]=="":
        if tic == True:
            bt4["text"]="X"
            tic  = False
        elif tic == False:
            bt4["text"]="0"
            tic = True
    pobeda()
    winn()
def b5():
    global tic
    if bt5["text"]=="":
        if tic == True:
            bt5["text"]="X"
            tic  = False
        elif tic == False:
            bt5["text"]="0"
            tic = True
    pobeda()
    winn()
def b6():
    global tic
    if bt6["text"]=="":
        if tic == True:
            bt6["text"]="X"
            tic  = False
        elif tic == False:
            bt6["text"]="0"
            tic = True
    pobeda()
    winn()
def b7():
    global tic
    if bt7["text"]=="":
        if tic == True:
            bt7["text"]="X"
            tic  = False
        elif tic == False:
            bt7["text"]="0"
            tic = True
    pobeda()
    winn()
def b8():
    global tic
    if bt8["text"] == "":
        if tic == True:
            bt8["text"]="X"
            tic  = False
        elif tic == False:
            bt8["text"]="0"
            tic = True
    pobeda()
    winn()
def b9():
    global tic
    if bt9["text"]=="":
        if tic == True:
            bt9["text"]="X"
            tic  = False
        elif tic == False:
            bt9["text"]="0"
            tic = True
    pobeda()
    winn()

def pobeda():
    if bt1["text"]=="X" and bt2["text"]=="X" and bt3["text"]=="X":
        print("podeba X")
    elif bt1["text"]==bt5["text"]==bt9["text"]=="X":
        print("podeba X")
    elif bt7["text"]==bt5["text"]==bt3["text"]=="X":
        print("podeba X")
    elif bt1["text"]==bt2["text"]==bt3["text"]=="X":
        print("podeba X")
    elif bt4["text"]==bt5["text"]==bt6["text"]=="X":
        print("podeba X")
    elif bt7["text"]==bt8["text"]==bt9["text"]=="X":
        print("podeba X")
    elif bt1["text"]==bt4["text"]==bt7["text"]=="X":
        print("podeba X")
    elif bt2["text"]==bt5["text"]==bt8["text"]=="X":
        print("podeba X")
    elif bt3["text"]==bt6["text"]==bt9["text"]=="X":
        print("podeba X")
def winn():
    if bt1["text"]=="0" and bt2["text"]=="0" and bt3["text"]=="0":
        print("podeba 0")
    elif bt1["text"]==bt2["text"]==bt3["text"]=="0":
        print("podeba 0")
    elif bt1["text"]==bt4["text"]==bt7["text"]=="0":
        print("podeba 0")
    elif bt2["text"]==bt5["text"]==bt8["text"]=="0":
        print("podeba 0")
    elif bt3["text"]==bt6["text"]==bt9["text"]=="0":
        print("podeba 0")
    elif bt4["text"]==bt5["text"]==bt6["text"]=="0":
        print("podeba 0")
    elif bt7["text"]==bt8["text"]==bt9["text"]=="0":
        print("podeba 0")
    elif bt1["text"]==bt5["text"]==bt9["text"]=="0":
        print("podeba 0")
    elif bt7["text"]==bt5["text"]==bt3["text"]=="0":
        print("podeba 0")
font_text = ("Arial",40,"bold")
win = Tk()
win.geometry("315x430+650+170")
bt0 = Button(win,font = font_text,width = 3,relief = RAISED,command = b1)
bt0.grid(row = 0,column = 0)

bt1 = Button(win,font = font_text,width = 3,relief = RAISED,command = b1)
bt1.grid(row = 0,column = 0)

bt2 = Button(win,font = font_text,width = 3,relief = RAISED,command = b2)
bt2.grid(row = 1,column = 0)

bt3 = Button(win,font = font_text,width = 3,relief = RAISED,command = b3)
bt3.grid(row = 2,column = 0)

bt4 = Button(win,font = font_text,width = 3,relief = RAISED,command = b4)
bt4.grid(row = 0,column = 1)

bt5 = Button(win,font = font_text,width = 3,relief = RAISED,command = b5)
bt5.grid(row = 1,column = 1)

bt6 = Button(win,font = font_text,width = 3,relief = RAISED,command = b6)
bt6.grid(row = 2,column = 1)

bt7 = Button(win,font = font_text,width = 3,relief = RAISED,command = b7)
bt7.grid(row = 0,column = 2)

bt8 = Button(win,font = font_text,width = 3,relief = RAISED,command = b8)
bt8.grid(row = 1,column = 2)

bt9 = Button(win,font = font_text,width = 3,relief = RAISED,command = b9)
bt9.grid(row = 2,column = 2)

enabled = IntVar()
them = Checkbutton(win,text="black",variable = enabled,command = black)
them.place(x=250,y=340)




label_1 = tkinter.Button(win, text="заново",
                        bg="#fbfcfc",
                        font = ("Times Nev Roman",20,"bold"),
                        relief=tkinter.RAISED,
                        command = label_1
                        )
label_1.place(x=100,y=350)
win.mainloop()

def change():
    if q.get() == 0:
        label['bg'] = "#2005f7"
    elif q.get() == 1:
        label['bg'] = "#2005f7"
    elif q.get() == 2:
        label['bg'] = "#2005f7"

blue = Radiobutton(text="Blue", variable=q, value={0,1,2})
Button = Button(text="Изменить", command=change)

bt0 = tkinter.Button(karobli,text = "поставить корабль",
                     bg="#2005f7",
                     command = karobli)

bt0.place(x=800,y=350)
'''
def karobli():
    for i in range(0,3):
        if q > 4:
            q[i]["text"] = ""
            print("у вас закончились корабльи на одну клетку ")
            
                qwe = 1
    elif q.get()==2:
        qwe = 2
    elif q.get() == 3:
        qwe = 2
    elif q.get() == 2:
        qwe = 4
'''
"""
"""
from tkinter import *


win = Tk()
win.geometry("1200x700+250+80")
q = IntVar()


odin  = 0
dva  = 0
tro = 0
chetire = 0
i = 0
vid = 0


def qwe():
    global vid

    if q.get() == 1:
        vid =1

    elif q.get() == 2:
        vid = 2

    elif q.get() == 3:
        vid = 3

    elif q.get() == 4:
        vid = 4

rd1 = Radiobutton(win, variable=q, value=1, text="корабль на одну клетку", command=qwe )
rd1.place(x=600,y=150)
rd2 = Radiobutton(win, variable=q, value=2, text="корабль на две клетки", command=qwe )
rd2.place(x=600,y=180)
rd3 = Radiobutton(win, variable=q, value=3, text="корабль на три клетки", command=qwe )
rd3.place(x=600,y=210)
rd4 = Radiobutton(win, variable=q, value=4, text="корабль на четыре клетки", command=qwe )
rd4.place(x=600,y=240)

b = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",
     11:"",12:"",13:"",14:"",15:"",16:"",17:"",18:"",19:"",20:"",
     21:"",22:"",23:"",24:"",25:"",26:"",27:"",28:"",29:"",30:"",
     31:"",32:"",33:"",34:"",35:"",36:"",37:"",38:"",39:"",40:"",
     41:"",42:"",43:"",44:"",45:"",46:"",47:"",48:"",49:"",50:"",
     51:"",52:"",53:"",54:"",55:"",56:"",57:"",58:"",59:"",60:"",
     61:"",62:"",63:"",64:"",65:"",66:"",67:"",68:"",69:"",70:"",
     71:"",72:"",73:"",74:"",75:"",76:"",77:"",78:"",79:"",80:"",
     81:"",82:"",83:"",84:"",85:"",86:"",87:"",88:"",89:"",90:"",
     91:"",92:"",93:"",94:"",95:"",96:"",97:"",98:"",99:"",100:"",}

def qqq(Button):
    global vid,odin,dva,b,tro,chetire
    print(vid)
    if vid ==1 and odin<4:

        Button["bg"] = "#3010fa"
        odin+=1

    if vid ==2 and dva<3:

        ar = str(Button).split('n')
        cletka = int(ar[1])
        b[cletka]["bg"] = "#3010fa"
        b[cletka - 1]["bg"] = "#3010fa"

        dva+=1

    if vid == 3 and tro<2:
        ar = str(Button).split('n')
        cletka = int(ar[1])
        b[cletka]["bg"] = "#3010fa"
        b[cletka - 1]["bg"] = "#3010fa"
        b[cletka - 2]["bg"] = "#3010fa"
        tro+=1

    if vid == 4 and chetire<1:



        ar=str(Button).split('n')
        cletka = int(ar[1])
        b[cletka]["bg"] = "#3010fa"
        b[cletka-1]["bg"] = "#3010fa"
        b[cletka-2]["bg"] = "#3010fa"
        b[cletka+1]["bg"] = "#3010fa"
        chetire+=1



def kor():

    global odin
    global vid
    if odin == 1:
        if vid > 4:
            Button["bg"] = "#3010fa"
            vid -=1

b[0] = Button(win,font = (40),width = 3,command =lambda: qqq(b[0]))
b[1] = Button(win,font = (40),width = 3,command =lambda: qqq(b[1]))
b[2] = Button(win,font = (40),width = 3,command =lambda: qqq(b[2]))
b[3] = Button(win,font = (40),width = 3,command =lambda: qqq(b[3]))
b[4] = Button(win,font = (40),width = 3,command =lambda: qqq(b[4]))
b[5] = Button(win,font = (40),width = 3,command =lambda: qqq(b[5]))
b[6] = Button(win,font = (40),width = 3,command =lambda: qqq(b[6]))
b[7] = Button(win,font = (40),width = 3,command =lambda: qqq(b[7]))
b[8] = Button(win,font = (40),width = 3,command =lambda: qqq(b[8]))
b[9] = Button(win,font = (40),width = 3,command =lambda: qqq(b[9]))
b[ 10 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 10 ]))
b[ 11 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 11 ]))
b[ 12 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 12 ]))
b[ 13 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 13 ]))
b[ 14 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 14 ]))
b[ 15 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 15 ]))
b[ 16 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 16 ]))
b[ 17 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 17 ]))
b[ 18 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 18 ]))
b[ 19 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 19 ]))
b[ 20 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 20 ]))
b[ 21 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 21 ]))
b[ 22 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 22 ]))
b[ 23 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 23 ]))
b[ 24 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 24 ]))
b[ 25 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 25 ]))
b[ 26 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 26 ]))
b[ 27 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 27 ]))
b[ 28 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 28 ]))
b[ 29 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 29 ]))
b[ 30 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 30 ]))
b[ 31 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 31 ]))
b[ 32 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 32 ]))
b[ 33 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 33 ]))
b[ 34 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 34 ]))
b[ 35 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 35 ]))
b[ 36 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 36 ]))
b[ 37 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 37 ]))
b[ 38 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 38 ]))
b[ 39 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 39 ]))
b[ 40 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 40 ]))
b[ 41 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 41 ]))
b[ 42 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 42 ]))
b[ 43 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 43 ]))
b[ 44 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 44 ]))
b[ 45 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 45 ]))
b[ 46 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 46 ]))
b[ 47 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 47 ]))
b[ 48 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 48 ]))
b[ 49 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 49 ]))
b[ 50 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 50 ]))
b[ 51 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 51 ]))
b[ 52 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 52 ]))
b[ 53 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 53 ]))
b[ 54 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 54 ]))
b[ 55 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 55 ]))
b[ 56 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 56 ]))
b[ 57 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 57 ]))
b[ 58 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 58 ]))
b[ 59 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 59 ]))
b[ 60 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 60 ]))
b[ 61 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 61 ]))
b[ 62 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 62 ]))
b[ 63 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 63 ]))
b[ 64 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 64 ]))
b[ 65 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 65 ]))
b[ 66 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 66 ]))
b[ 67 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 67 ]))
b[ 68 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 68 ]))
b[ 69 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 69 ]))
b[ 70 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 70 ]))
b[ 71 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 71 ]))
b[ 72 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 72 ]))
b[ 73 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 73 ]))
b[ 74 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 74 ]))
b[ 75 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 75 ]))
b[ 76 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 76 ]))
b[ 77 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 77 ]))
b[ 78 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 78 ]))
b[ 79 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 79 ]))
b[ 80 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 80 ]))
b[ 81 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 81 ]))
b[ 82 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 82 ]))
b[ 83 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 83 ]))
b[ 84 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 84 ]))
b[ 85 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 85 ]))
b[ 86 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 86 ]))
b[ 87 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 87 ]))
b[ 88 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 88 ]))
b[ 89 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 89 ]))
b[ 90 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 90 ]))
b[ 91 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 91 ]))
b[ 92 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 92 ]))
b[ 93 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 93 ]))
b[ 94 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 94 ]))
b[ 95 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 95 ]))
b[ 96 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 96 ]))
b[ 97 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 97 ]))
b[ 98 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 98 ]))
b[ 99 ] = Button(win,font = (40),width = 3,command =lambda: qqq(b[ 99 ]))



for i in range(0,10):
    b[i].grid(row=0,column = i)
for i in range(10,20):
    b[i].grid(row=1,column = i-10)
for i in range(20,30):
    b[i].grid(row=2,column = i-20)
for i in range(30,40):
    b[i].grid(row=3,column = i-30)
for i in range(40,50):
    b[i].grid(row=4,column = i-40)
for i in range(50,60):
    b[i].grid(row=5,column = i-50)
for i in range(60,70):
    b[i].grid(row=6,column = i-60)
for i in range(70,80):
    b[i].grid(row=7,column = i-70)
for i in range(80,90):
    b[i].grid(row=8,column = i-80)
for i in range(90,100):
    b[i].grid(row=9,column = i-90)
padx
pady
bind("<Motion>",on_leave)
Motion
mainloop()
"""
""">",o
#скример
from tkinter import *

win =Tk()
win.geometry("1288x650")





def on_leave(event):
    button.place(x=0,y=550)
    button1.place(x=0, y=0)
    button2.place(x=0, y=0)
    button3.place(x=1090, y=0)
    button4.place(x=300, y=0)
    button5.place(x=500, y=250)
    button6.place(x=700, y=0)
    button7.place(x=900, y=250)
    button8.place(x=170, y=100)
    button9.place(x=200, y=400)
    button10.place(x=160, y=350)
    button11.place(x=200, y=300)
    button12.place(x=160, y=250)
    button13.place(x=240, y=180)
    button14.place(x=240, y=205)


    win.destroy()
from tkinter import messagebox
def pobeda():
    messagebox.showinfo("dfa","dg")
button = Button(win,text = "",
                padx=635,
                pady=80,
                bg="#050505",
                relief = FLAT)
button1 = Button(win,text = "",
                 padx=80,
                 pady=355,
                 bg="#050505",
                 relief = FLAT)
button2 = Button(win,text = "",
                 padx=635,
                 pady=80,
                 bg="#050505",
                 relief = FLAT)
button3 = Button(win,text = "старт",
                 padx=80,
                 pady=355,
                 bg="#ffffff")
button4 = Button(win,text = "",
                 padx=30,
                 pady=220,
                 bg="#050505",
                 relief = FLAT)
button5 = Button(win,text = "",
                 padx=30,
                 pady=220,
                 bg="#050505",
                 relief = FLAT)
button6 = Button(win,text = "",
                 padx=30,
                 pady=220,
                 bg="#050505",
                 relief = FLAT)
button7 = Button(win,text = "",
                 padx=30,
                 pady=220,
                 bg="#050505",
                 relief = FLAT)
button8 = Button(win,text = "",
                 padx=30,
                 pady=30,
                 bg="#ff0000",
                 relief = FLAT,
                 command = pobeda)
button9 = Button(win,text = "",
                 padx=50,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)
button10 = Button(win,text = "",
                 padx=50,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)
button11 = Button(win,text = "",
                 padx=50,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)
button12 = Button(win,text = "",
                 padx=50,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)
button13 = Button(win,text = "",
                 padx=30,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)
button14 = Button(win,text = "",
                 padx=30,
                 pady=1,
                 bg="#050505",
                 relief = FLAT)




button.place(x=0,y=550)
button1.place(x=0,y=0)
button2.place(x=0,y=0)
button3.place(x=1090,y=0)
button4.place(x=300,y=0)
button5.place(x=500,y=250)
button6.place(x=700,y=0)
button7.place(x=900,y=250)
button8.place(x=170,y=100)
button9.place(x=200,y=400)
button10.place(x=160,y=350)
button11.place(x=200,y=300)
button12.place(x=160,y=250)
button13.place(x=240,y=180)
button14.place(x=240,y=205)
button.bind("<Motion>",on_leave)
button1.bind("<Motion>",on_leave)
button2.bind("<Motion>",on_leave)
button4.bind("<Motion>",on_leave)
button5.bind("<Motion>",on_leave)
button6.bind("<Motion>",on_leave)
button7.bind("<Motion>",on_leave)
button9.bind("<Motion>",on_leave)
button10.bind("<Motion>",on_leave)
button11.bind("<Motion>",on_leave)
button12.bind("<Motion>",on_leave)
button13.bind("<Motion>",on_leave)
button14.bind("<Motionn_leave)

def on_leave(event):
    button.place(x=0,y=0)
    button1.place(x=9,y=0)
    button2.place(x=18,y=0)
    button3.place(x=27,y=0)


button = Button(win,text = "",
                padx=-10,
                pady=0,
                relief = FLAT)

button1 = Button(win,text = "",
                padx=-10,
                pady=0,
                relief = FLAT)

button2 = Button(win,text = "",
                padx=-10,
                pady=0,
                relief = FLAT)

button3 = Button(win,text = "",
                padx=-10,
                pady=0,
                relief = FLAT)

button.place(x=0,y=0)
button1.place(x=9,y=0)
button2.place(x=18,y=0)
button3.place(x=27,y=0)
button.bind("<Motion>",on_leave)
button1.bind("<Motion>",on_leave)
button2.bind("<Motion>",on_leave)
button3.bind("<Motion>",on_leave)




win.mainloop()
"""
"""
from tkinter import *
win = Tk()
win.geometry("500x500")
btn = []
d = 0
for i in range(0,2500):
    btn.append(Button(win,width  =2))

for i in range(0,50):
    for j in range(0,50):
        btn[i*50 + j].grid(row = i,column = j)
def red(event):
    event.widget["bg"]="red"
for i in range(0,2500):
    btn[i].bind('<Motion>',red)


def qwe():
    if d == "colour = #0000ff00":
        print("")



    rd1 = Radiobutton(win, variable=d, value=1, text="синий", command=qwe)
    rd1.place(x=1900, y=10)

win.mainloop()
"""
"""
from tkinter import *
win = Tk()
btns = []
for i in range (0,56):
    btns.append(Button(win,width = 8, height= 4))
for i in range (0,7):
    for j in range (0,8):
        btns [i*8 +j].grid(row = i, column = j)
        btns[i * 8 + j]["text"]=i*8+j
def ramki():
    btns[1]["text"]="1-2"
    btns[2]["text"]="1-3"
    btns[3]["text"]="1-4"
    btns[4]["text"]="1-5"
    btns[5]["text"]="1-6"
    btns[6]["text"]="1-7"
    btns[7]["text"]="1-8"
    btns[8]["text"]="10.00-11.40"
    btns[16]["text"]="11.50-13.20"
    btns[24]["text"]="13.40-14.25"
    btns[32]["text"]="15.20-16.05"
    btns[40]["text"]="16.10-16.55"
    btns[48]["text"]="18.40-20.15"
def ochistka():
    for i in range(0, 7):
        for j in range(0, 8):
            btns[i * 8 + j]["bg"] = "SystemButtonFace"
            btns[i * 8 + j]["text"] = ""
    ramki()


def monday():
    ochistka()
    btns[19]["bg"]="gray"
    btns[19]["text"]="андроид\nОпарина"
    btns[15]["bg"]="red"
    btns[15]["text"]="App Inventor\nОпарина"
    btns[14]["bg"]="gray"
    btns[22]["bg"]="gray"
    btns[27]["bg"]="gray"
    btns[27]["text"]="Java\nБатаев "
    btns[23]["bg"]="red"
    btns[23]["text"]="App Inventor\nОпарина,Батаев\nPython"
    btns[22]["text"]="WebDev\nМакаренко "
    btns[25]["bg"]="gray"
    btns[25]["text"]="Мем стори\nНикитин"
    btns[9]["bg"]="gray"
    btns[9]["text"]="ARDUNO 4U\nНикитин "
    btns[17]["bg"]="gray"
    btns[17]["text"]="ARDUNO 4U\nНикитин "
    btns[33]["bg"]="gray"
    btns[33]["text"]="ARDUNO 4U\nНикитин "
    btns[10]["bg"]="gray"
    btns[10]["text"]="Pixel\nСущевич "
    btns[18]["bg"]="gray"
    btns[26]["bg"]="gray"
    btns[34]["bg"]="gray"
    btns[37]["bg"]="gray"
    btns[38]["bg"]="gray"
    btns[38]["text"]="GameDev\nМакаренко "
def tuesday():
    ochistka()
    btns[23]["bg"]="gray"
    btns[19]["text"]="GameDev\nМакаренко,Михадок\nнейросети"
    btns[19]["bg"]="red"
    btns[15]["bg"]="gray"
    btns[27]["bg"]="gray"
    btns[27]["text"]="GameDev\nМакаренко "
    btns[35]["bg"]="gray"
    btns[46]["bg"]="gray"
    btns[33]["bg"]="gray"
    btns[18]["bg"]="gray"
    btns[9]["bg"]="gray"
    btns[17]["bg"]="gray"
    btns[25]["bg"]="gray"
    btns[10]["bg"]="gray"
    btns[41]["bg"]="gray"
    btns[41]["text"]="Виртуальный язык\nЧеркасов"
    btns[55]["bg"]="gray"
    btns[55]["text"]="Работотехника\nЧеркасов"
    btns[34]["bg"]="gray"
    btns[34]["text"]="C#\nБатаев"
    btns[26]["bg"]="gray"
    btns[26]["text"]="Pixel\nСущевич"
    btns[18]["bg"]="gray"
    btns[18]["text"]="Pixel\nСущевич"
    btns[13]["bg"]="gray"
    btns[13]["text"]="Системное администрирование\nСущевич"
    btns[42]["bg"]="gray"
    btns[42]["text"]="Юный програмист \nДетина"
def sreda():
    ochistka()
    btns[23]["bg"]="gray"
    btns[23]["text"]="App Inventor\nОпарина"
    btns[15]["bg"]="red"
    btns[15]["text"]="App Inventor,Python\nОпарина,Батаев"
    btns[18]["bg"]="gray"
    btns[27]["bg"]="gray"
    btns[27]["text"]="Java\nБатаев"
    btns[34]["bg"]="gray"
    btns[34]["text"]="C++\nБатаев"
    btns[30]["bg"]="gray"
    btns[13]["bg"]="gray"
    btns[13]["text"]="ARDUNO 4U\nНикитин"
    btns[21]["bg"]="gray"
    btns[21]["text"]="ARDUNO 4U\nНикитин"
    btns[33]["bg"]="gray"
    btns[33]["text"]="ЭлектроГрад\nНикитин"
    btns[41]["bg"]="gray"
    btns[41]["text"]="ЭлектроГрад\nНикитин"
    btns[10]["bg"]="gray"
    btns[17]["bg"]="gray"
    btns[26]["bg"]="gray"
    btns[35]["bg"]="gray"
    btns[35]["text"]="Ю Ф\nХодоскин"
    btns[43]["bg"]="gray"
    btns[43]["text"]="Ю Ф\nХодоскин"
    btns[19]["bg"]="gray"
    btns[19]["text"]="Графический дезайн \nЮрис"
    btns[25]["bg"]="gray"
    btns[25]["text"]="Мем стори \nНикитин"
def chetverg():
    ochistka()
    btns[23]["bg"]="gray"
    btns[23]["text"]="ПОА\nОпарина"
    btns[18]["bg"]="gray"
    btns[18]["text"]="Графический дезайн\nОпарина"
    btns[26]["bg"]="gray"
    btns[26]["text"]="Ю И\nОпарина"
    btns[14]["bg"]="red"
    btns[19]["bg"]="red"
    btns[27]["bg"]="gray"
    btns[31]["bg"]="gray"
    btns[34]["bg"]="gray"
    btns[45]["bg"]="gray"
    btns[53]["bg"]="gray"
    btns[9]["bg"]="gray"
    btns[43]["bg"]="gray"
    btns[15]["bg"]="gray"


def patniza():
    ochistka()
    btns[14]["bg"]="gray"
    btns[22]["bg"]="red"
    btns[30]["bg"]="gray"
    btns[23]["bg"]="red"
    btns[31]["bg"]="red"
    btns[34]["bg"]="gray"
    btns[37]["bg"]="gray"
    btns[45]["bg"]="gray"
    btns[53]["bg"]="gray"
    btns[39]["bg"]="gray"
    btns[10]["bg"]="gray"
    btns[42]["bg"]="gray"


def subota():
    ochistka()
    btns[10]["bg"]="gray"
    btns[18]["bg"]="gray"
    btns[26]["bg"]="gray"
    btns[34]["bg"]="gray"
    btns[42]["bg"]="gray"
    btns[31]["bg"]="gray"
    btns[39]["bg"]="gray"
    btns[47]["bg"]="gray"
    btns[27]["bg"]="gray"
    btns[22]["bg"]="gray"
    btns[41]["bg"]="gray"

def voaskresenie():
    ochistka()
    btns[17]["bg"]="red"
    btns[41]["bg"]="gray"
    btns[14]["bg"]="gray"
    btns[15]["bg"]="red"
    btns[55]["bg"]="gray"
    btns[23]["bg"]="gray"
    btns[31]["bg"]="gray"
    btns[47]["bg"]="gray"
    btns[34]["bg"]="gray"
    btns[42]["bg"]="gray"
    btns[9]["bg"]="gray"
    btns[21]["bg"]="gray"
    btns[29]["bg"]="gray"
    btns[30]["bg"]="gray"
    btns[38]["bg"]="gray"
    btns[46]["bg"]="gray"
    btns[54]["bg"]="gray"
    btns[22]["bg"]="gray"
    btns[26]["bg"]="gray"
    btns[10]["bg"]="gray"
    btns[18]["bg"]="gray"
q=IntVar()
def d_o_w():
    if q.get()  == 1:
        monday()
    elif q.get() == 2:
        tuesday()
    elif q.get() == 3:
        sreda()
    elif q.get() == 4:
        chetverg()
    elif q.get() == 5:
        patniza()
    elif q.get() == 6:
        subota()
    elif q.get() == 7:
        voaskresenie()

rd1 = Radiobutton(win, text ="ПН", value=1,variable =q, command = d_o_w)
rd1.place(x=700,y=150)
rd2 = Radiobutton(win, text ="ВТ", value=2,variable =q, command = d_o_w)
rd2.place(x=700,y=170)
rd3 = Radiobutton(win, text ="СР", value=3,variable =q, command = d_o_w)
rd3.place(x=700,y=190)
rd4 = Radiobutton(win, text ="ЧТ", value=4,variable =q, command = d_o_w)
rd4.place(x=700,y=210)
rd5 = Radiobutton(win, text ="ПТ", value=5,variable =q, command = d_o_w)
rd5.place(x=700,y=230)
rd6 = Radiobutton(win, text ="СБ", value=6,variable =q, command = d_o_w)
rd6.place(x=700,y=250)
rd7 = Radiobutton(win, text ="ВС", value=7,variable =q, command = d_o_w)
rd7.place(x=700,y=270)

label_1=Label(win,width= 37,height= 10, text = "qwe",relief= RAISED)


label_1.place(x=0,y=500)
ramki()
win.mainloop()

"""
from tkinter import *
win = Tk()
win.geometry("700x700")

file = open("../../Desktop/Дима литвинов/seif.txt", "r+")
i = int(file.read())
print(i)
count_clikk = 1

def clikk(event):
    global i, count_clikk
    i += count_clikk
    label_2["text"] = i

    label_1["width"] = 1
    label_1["height"] = 1
    label_5["width"] = 360
    label_5["height"] = 360
    label_4.place(x=500,y=400)
    label_4.place(x=random.randint(220,570),y=random.randint(250,570))



def qwe():
    global i, count_clikk
    if i >= 100:
        count_clikk += 1
        i-=100
    label_3.place(x=100000,y=10000000)

def add_clikk(event):
    label_1["width"] = 360
    label_1["height"] = 360
    label_5["width"] = 360
    label_5["height"] = 360
    label_4.place(x=500,y=400)
def asd():

    print(q.get())

    if q.get()== 1:
        print("a b c ")
    elif q.get()==2:
        print("c b a")

q = IntVar()

rd1 = Radiobutton(win, text ="", value=1,variable =q, command = asd)
rd1.place(x=500,y=150)

rd2 = Radiobutton(win, text ="", value=2,variable =q, command = asd)
rd2.place(x=600,y=150)
image_Button = PhotoImage(file ="../../Desktop/Дима литвинов/360fx360f.png")
image_Button1 = PhotoImage(file ="855860383_preview_Gsg-9-model.png")
#создать вторую картинку по примеру выше
#чтоб выставить в функции asd : label_1["iamge"] = name
label_5 = tkinter.Label(win, text="кнопка",
                        #bg="#FFFFFF",
                        font = ("Times Nev Roman",20,"bold"),
                        image=image_Button1,
                        )

label_1 = tkinter.Label(win, text="кнопка",
                        #bg="#FFFFFF",
                        font = ("Times Nev Roman",20,"bold"),
                        image=image_Button,
                        )

label_4 = tkinter.Label(win,text = "+1")
label_4.place(x=500,y=210)
label_1.bind("<Button-1>",clikk)
label_1.bind("<ButtonRelease>",add_clikk)
label_5.bind("<Button-1>",clikk)
label_5.bind("<ButtonRelease>",add_clikk)
label_2 = tkinter.Label(win, text=i,
                        bg="#FFFFFF",
                        font = ("Times Nev Roman",20,"bold"),
                        width=15,
                        height=1,
                        )

label_3 = tkinter.Button(win,
                         text="x2",
                         command=qwe,
                         )


label_1.place(x=170,y=270)
label_2.place(x=220,y=50)
label_3.place(x=600,y=100)
label_5.place(x=170,y=250)
win.mainloop()

file1 = open("../../Desktop/Дима литвинов/seif.txt", "w+")
file1.write(str(i))
"""

from tkinter import *

win = Tk()
q = IntVar()
def qwe():
    print(q.get())
    if q.get() == 1:
        print("")
    elif q.get() == 2:
        print("")
    elif q.get() == 3:
        print("")

rd1 = Radiobutton(win,variable = q,value = 1,text = "1",command = qwe).pack()
rd2 = Radiobutton(win,variable = q,value = 2,text = "2",command  =qwe).pack()
rd3 = Radiobutton(win,variable = q,value = 3,text = "3",command = qwe).pack()

mainloop()

"""
"""
t= True
while t:
    try:
        s = input()
        file = open(s, 'r')
        t = False
        print("такой файл есть")
        if s == "exzit":
            t = False


    except FileNotFoundError:
        print("такого файла нет,попробуйте ещё")
"""