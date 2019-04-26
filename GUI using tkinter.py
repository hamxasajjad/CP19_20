### Libraries ###
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import StringVar
from tkinter import *


root = tk.Tk()
form = Frame(root)
form.grid()

### Size ###
root.geometry("150x390")
root.title("Testing Program")

tv1 = StringVar()

### Fuctions ###
def helloCallBack():
    messagebox.showinfo("Hello GUI" , tv1.get())
    tv1.get("ok")
    
def helloCallBack2():
    messagebox.showinfo("Hello GUI" , "Hello World")


### Label ###
L1 = tk.Label(form,text = "Heading")
L1.grid(row=1,column=1,padx=15, pady = 15)
    
### Buttons ###    
B1 = tk.Button(form, text="Click Me", height = 5, width = 10 , bg = "Red" , fg = "white", command = helloCallBack)
B1.grid(row=3,column=1,padx=30, pady = 30)

B2 = tk.Button(form, text="Click Me 2", height = 5, width = 10 , bg = "Blue" , fg = "white", command = helloCallBack2)
B2.grid(row=4,column=1,padx=30, pady = 30)

### Input ###
t1 = tk.Entry (form, textvariable = tv1 )
t1.grid (row = 2 , column = 1)




#B1.pack()
#B2.pack()
#L1.pack()

root.mainloop()
