import cv2
import numpy as np
import dlib
from tkinter import *
import sys
import time
from PIL import Image, ImageTk


root = Tk()
root.geometry("1000x600")
root.title("Exam Cheating Identifier  v1.0")
root.iconbitmap('fav.ico')

#functions

def prnt():
    print("Testing")
    
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)
    
def fd():
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    while True:
        ret,frame=cap.read()
        frame = cv2.flip(frame,1)    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=detector(gray)
        for face in faces:
            x,y=face.left(),face.top()
            w,h=face.right(),face.bottom()
        
            cv2.rectangle(frame,(x,y),(w,h),(0,225,0),3)
       # cv2.imshow("gray",gray)
        cv2.imshow("frame",frame)
    
        if cv2.waitKey(1) == ord("s"):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
# Frames


f2 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f2.pack(side = TOP, fill="x")


f3 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f3.pack(side = BOTTOM, fill="x")

f1 = Frame(root, bg = "silver", borderwidth = 6 , relief = GROOVE)
f1.pack(side = RIGHT, fill="y")


#Labels
l1 = Label(f1, text = "    "*25, bg = "silver" )
l1.pack()
l1a = Label(f1, text = " STUDENTS RECORD ",
           bg = "silver" , fg = "black" , font = ("Berlin Sans FB Demi",20,"bold") )
l1a.pack()
l1b = Label(f1, text = " Marks Deduction ",
           bg = "silver" , fg = "black" , font = ("Arial",10,"bold") )
l1b.pack()


l2 = Label(f2, text = "                EXAM CHEATING IDENTIFIER                  ",
           bg = "silver" , fg = "black" , font = ("Berlin Sans FB Demi",30,"bold") )
l2.pack()

l3 = Label(f3, text = "Members:   M.Hamza,  Fouzan,  Waqas,  Haris,  Zeeshan   ", bg = "silver"  )
l3.pack(side=LEFT)
l3a = Label(f3, text = "Instructor:  Sir Roohan ? ", bg = "silver"  )
l3a.pack(side=RIGHT)

l4 = Label(root, text = " Here will be your live streaming screen " )
l4.pack()

clock=Label(root, font=("times", 10, "bold"), fg="green")
clock.pack(anchor="se",side=BOTTOM)
tick()

# Student images icon
photo = PhotoImage(file="2.png")
img1 = Label(f1, image=photo, bg="silver")
img1.pack(pady=2,padx=15, anchor="nw")
seat1 = Label(f1, text="Seat# 1",bg="silver",font=("Arial",10,"bold")).pack(pady=0,padx=18,anchor="nw")

img2 = Label(f1, image=photo, bg="silver")
img2.pack(pady=2,padx=15, anchor="nw")
seat2 = Label(f1, text="Seat# 2",bg="silver",font=("Arial",10,"bold")).pack(pady=0,padx=18, anchor="nw")

img3 = Label(f1, image=photo, bg="silver")
img3.pack(pady=2,padx=15, anchor="nw")
seat3 = Label(f1, text="Seat# 3",bg="silver",font=("Arial",10,"bold")).pack(pady=0,padx=18, anchor="nw")

#image in root
#image_root = Image.open("sir.jpg")
#photo_root = ImageTk.PhotoImage(image_root)

#img_root = Label(root, image = photo_root)
#img_root.pack()


#Buttons
B1 = Button(f1,text="Start", bg="gray", fg="white", height=2 , width=15,font=("Arial",10,"bold"), command=fd)
B1.pack(side=LEFT,pady=20, padx=15, anchor="se")
B2 = Button(f1,text="Quit", bg="gray", fg="white", height=2 , width=15,font=("Arial",10,"bold"),command=root.destroy)
B2.pack(side=RIGHT,pady=20,padx=15,anchor="sw")

#WIDGET
#B2.bind("<Button-1>",exit)
root.mainloop()