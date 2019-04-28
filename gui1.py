from tkinter import *
root= Tk()
l1=Label(root,text="Username")
l2=Label(root,text="Password")
entry1= Entry(root)
entry2= Entry(root)
l1.grid(row=0)
l2.grid(row=1)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
def C():
    messagebox.showinfo("Welcome" , entry1.get())
B1 = tk.Button(root, text="Submit", height = 2, width = 8 , bg = "Blue" , fg = "white",command =C)
B1.grid(row=2,column=2,padx=30, pady = 30)

root.mainloop()
