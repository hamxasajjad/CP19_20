import cv2
import numpy as np
import dlib
from tkinter import *
import tkinter.messagebox
import time
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
ret,frame=cap.read()
detector = dlib.get_frontal_face_detector()
count =0
marks =0
root = Tk()
root.geometry("975x585")
root.title("Exam Cheating Identifier  v1.1")
root.iconbitmap('fav.ico')

#i = StrVar()
#i = 0
#j = StrVar()
#j = 0

tbt= StringVar()


#functions

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    fd()
    clock.after(200, tick)
    
def inst():
    tkinter.messagebox.showinfo('Rules Of Exams',' *. Look Straight Into Your Computer Screen \n *. -1 will be deducted on 5 points each ')


def fd():
    global count
    global marks
    
    ret,frame=cap.read()
    frame = cv2.flip(frame,1)  
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    
    x = 0
    y = 0
    for face in faces:
        x,y=face.left(),face.top()
        w,h=face.right(),face.bottom()
        cv2.rectangle(frame,(x,y),(w,h),(0,225,0),3)
       
       
    if (x == 0) and (y == 0):
        print((x,y),"No Face")
        count = count - 1
        print(count)
        if count == -5:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -10:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -15:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -20:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -25:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -30:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -35:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -40:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -45:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -50:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -55:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -60:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -65:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -70:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -75:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -80:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -85:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -90:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -95:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
        if count == -100:
            marks = marks - 1
            txt2.insert(0.0,marks)
            txt2.delete(0.0,'end')
            txt2.insert(0.0,marks)
    
    else:
        print((x,y),"Face")
        txt.insert(0.0,count)
        txt.delete(0.0,'end')
        txt.insert(0.0,count)
    
    im1 = Image.fromarray(frame)     
    photo_root = ImageTk.PhotoImage(im1)
    img_root.config(image = photo_root)
    img_root.image = photo_root
    txt.insert(0.0,count)
    txt.delete(0.0,'end')
    txt.insert(0.0,count)
   
        
    

    

f2 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f2.pack(side = TOP, fill="x")


f3 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f3.pack(side = BOTTOM, fill="x")

f1 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f1.pack(side = RIGHT, fill="y")




#Labels
l1 = Label(f1, text = "    "*2, bg = "silver" )
l1.pack()
l1a = Label(f1, text = " STUDENTS RECORD ",
           bg = "silver" , fg = "black" , font = ("Berlin Sans FB Demi",20,"bold") )
l1a.pack()
l1b = Label(f1, text = " Marks Deduction ",
           bg = "silver" , fg = "black" , font = ("Arial",10,"bold") )
l1b.pack()
l1c = Label(f1, text = "  ",
           bg = "silver" , fg = "black" , font = ("Arial",10,"bold") )
l1c.pack()

l2 = Label(f2, text = "                EXAM CHEATING IDENTIFIER                  ",
           bg = "silver" , fg = "black" , font = ("Berlin Sans FB Demi",30,"bold") )
l2.pack()

l3 = Label(f3, text = "Members:   M.Hamza,  Fouzan,  Waqas,  Haris,  Zeeshan   ", bg = "silver"  )
l3.pack(side=LEFT)
l3a = Label(f3, text = "Instructor:  Sir Roohan ❤ ", bg = "silver"  )
l3a.pack(side=RIGHT)


clock=Label(f3, font=("times", 10, "bold"), fg="green", bg="silver")
clock.pack(anchor=S,side=BOTTOM )

# Student images icon
photo = PhotoImage(file="2.png")
img1 = Label(f1, image=photo, bg="silver")
img1.pack(pady=2,padx=15)
seat1 = Label(f1, text="Deducted Points",bg="silver",font=("Arial",10,"italic")).pack(pady=0,padx=18)

img_root = Label(root, text = "Live Streaming")
img_root.pack()

### Text
txt = Text(f1, height = 1, width = 3,bg = "silver",fg = "red", font=("Arial",30,"bold"))
txt.pack()

l1d = Label(f1, text = " Marks Deducted ",
           bg = "silver" , fg = "black" , font = ("Arial",10,"bold") )
l1d.pack()

txt2 = Text(f1, height = 1, width = 3,bg = "silver",fg = "red", font=("Arial",30,"bold"))
txt2.pack(pady = 5)

l1e = Label(f1, text = "  ",
           bg = "silver" , fg = "black" , font = ("Arial",10,"bold") )
l1e.pack()

#Buttons
B1 = Button(f1,text="Instructions", bg="gray", fg="white", height=1 , width=35,font=("Arial",10,"bold"), command=inst)
B1.pack(pady=0, padx=15)
B2 = Button(f1,text="Start", bg="gray", fg="white", height=2 , width=15,font=("Arial",10,"bold"), command=tick)
B2.pack(side=LEFT,pady=15, padx=15, anchor="se")
B3 = Button(f1,text="Quit", bg="gray", fg="white", height=2 , width=15,font=("Arial",10,"bold"),command=root.destroy)
B3.pack(side=RIGHT,pady=15,padx=15,anchor="sw")


root.mainloop()

cap.release()
