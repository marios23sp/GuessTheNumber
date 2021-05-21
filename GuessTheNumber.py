from tkinter import *
from tkinter.ttk import *
import random

win= Tk()
win.geometry('275x400')

logo1= PhotoImage(file= "uparrow.png")
logo2= PhotoImage(file= "downarrow.png")
logo3= PhotoImage(file= "check.png")
logo1= logo1.subsample(2)
logo2= logo2.subsample(2)
logo3= logo3.subsample(2)

def Exit():
    win.destroy()

def restart():
    global a
    txt1.delete(0, "end")
    a = random.randint(0, 100)
    lbl3.configure(image= "")

a = random.randint(0, 100)

def Check(*args):
    global a

    lbl3.configure(image= "")

    if int(txt1.get())> a:
        lbl3.configure(image= logo2)

    elif int(txt1.get())< a:
        lbl3.configure(image= logo1)

    elif int(txt1.get())== a:
        lbl3.configure(image= logo3)

    txt1.delete(0, "end")

lbl1= Label(win, text= "Guess the Number")
lbl1.grid(column= 1, row= 0)

lbl2= Label(win, text= "Try to guess the number!")
lbl2.grid(column= 1, row= 2)

lbl3= Label(win, image= "")
lbl3.grid(column= 1, row= 4)

txt1= Entry(win, width= 15)
txt1.grid(column= 1, row= 6)

btn2= Button(win, text= "Exit", command= Exit)
btn2.grid(column= 1, row= 8)

btn1= Button(win, text= "Restart", command= restart)
btn1.grid(column= 1, row= 9)

win.bind('<Return>', Check)

win.mainloop()