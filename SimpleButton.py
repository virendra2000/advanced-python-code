from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Friends Name");
root.geometry('320x320')
frm=Frame(root)
frm.pack(fill=BOTH)
Button(frm,text="Virendra",fg="red").pack(side=LEFT)
Button(frm,text="Ameya",fg="green").pack(side=RIGHT)
Button(frm,text="Rahul",fg="blue").pack(side=LEFT)
Button(frm,text="Pratik",fg="violet").pack(side=RIGHT)
Button(frm,text="Roshni",fg="indigo").pack(side=LEFT)
Button(frm,text="Sonal",fg="orange").pack(side=RIGHT)
Button(frm,text="Rutuja",fg="green").pack(side=LEFT)
Button(frm,text="Vaishnavi",fg="red").pack(side=LEFT)
root.mainloop()
