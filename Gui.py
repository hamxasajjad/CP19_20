

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("400x300")
t=Label(top,text="Please Enter Your Name")
e=Entry(top,bd=5,)
t.grid(row=2,)
e.grid(row=2,column=1)
def message():
   msg = messagebox.showinfo( "Hello", e.get())

B = Button(top, text = "Submit", command = message,height=3,width=10,bg="gray",fg="white")
B.place(x = 150,y = 100)
B.flash()
top.mainloop()

