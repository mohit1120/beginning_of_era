from tkinter import *
def add():
    s1=e1.get()
    s2=e2.get()
    try:
        x=(s1+" ")
        y=(s2)
        z=x+y
        v1.set(z)
        
    except Exception as e:
            v2.set("Error: Invalid inputs")
    return
window=Tk()
v1=StringVar()
v2=StringVar()
l1=Label(window,text="Enter your fisrt name:")
e1=Entry(window)
l2=Label(window,text="Enter your last name:")
e2=Entry(window)
l3=Label(window,text="Name after concatenation:")
e3=Entry(window,textvariable=v1)
b1=Button(window,text="CONCATENATION",command=add)
msg=Label(window,fg="red",textvariable=v2)

l1.grid(row=0,column=0)
e1.grid(row=1,column=0)
l2.grid(row=0,column=1)
e2.grid(row=1,column=1)
l3.grid(row=0,column=2)
e3.grid(row=1,column=2)
b1.grid(row=3,column=1)
msg.grid(row=2,column=0)
