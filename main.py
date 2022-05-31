from tkinter import*
from tkinter import ttk   
import tkinter                             
from tkinter import font                 
from PIL import Image,ImageTk                   
import os
from student import Student
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from chatbot import ChatBot

class Face_Recognition_System :   

    def iExit(self) :
            self.iExit = tkinter.messagebox.askyesno("Face Recognition System","Do you Really Want to Exit ?",parent=self.root)
            if self.iExit > 0 :
                self.root.destroy()
            else :
                return

    def help(self) :
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def attendance_data(self):                                    
        self.new_window=Toplevel(self.root)         
        self.app=Attendance(self.new_window) 

    def face_data(self):                                    
        self.new_window=Toplevel(self.root)         
        self.app=Face_Recognition(self.new_window)                  
    
    def train_data(self):                                    
        self.new_window=Toplevel(self.root)         
        self.app=Train(self.new_window)

    #Making a Function to make the link between the button and the page
    def stud_details(self):                                     #def is the default keyword to make the function
        self.new_window=Toplevel(self.root)         #will make the new window
        self.app=Student(self.new_window)


    def __init__(self,root) :           #Callling the constructor and the root in the screen name
        self.root = root                                        #initalizing root
        self.root.geometry("1410x680+0+0")              #Size of the Window
        self.root.title("Face Recognition System")              

        #BACKGROUND IMAGE
        b_img = Image.open(r"images/FirstBg.png")         
        b_img = b_img.resize((1410,680),Image.ANTIALIAS)  #Storing Image into a Variable
        self.b_image = ImageTk.PhotoImage(b_img)  
    
        bg_image = Label(self.root,image = self.b_image) 
        bg_image.place(x=0,y=0,width=1410,height=680) 

        #Time
        def time() :
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(self.root, font=("Terminal",15,"bold"))
        lbl.place(x=10,y=55,width=150,height=50)
        time()

        #FIRST BUTTON STUDENT DETAILS          
        b1 = Button(bg_image,text="Student Management System",command=self.stud_details,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b1.place(x=190,y=250,width=360,height=40)

        #SECOND BUTTON FACE DETECTOR        
        b2 = Button(bg_image,text="Take Attendance",command=self.face_data,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b2.place(x=190,y=390,width=360,height=40)

        #THIRD BUTTON ATTENDENCE        
        b3 = Button(bg_image,text="Attendence Management System",command=self.attendance_data,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b3.place(x=190,y=320,width=360,height=40)

        #FOURTH BUTTON ABOUT-US  
        b3 = Button(bg_image,text="Train Data",command=self.train_data,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b3.place(x=190,y=460,width=360,height=40)

        #FIFTH BUTTON TRAIN DATA
        b4 = Button(bg_image,text="F.A.Q",command=self.help,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b4.place(x=190,y=540,width=360,height=40)

        #SIXTH BUTTON EXIT        
        b3 = Button(bg_image,text="Exit",command=self.iExit,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b3.place(x=1100,y=540,width=220,height=40)

        #Thia Function will show the stored cropped Gray images taken by webcam.
        #We Just Have to Call this Function in the Command Parameter of any Button and the Popup Windows will be open.
        def open_image(self):
            os.startfile("data/")


if __name__ == "__main__":                  #CALLING THE MAIN
    root = Tk()                                 #CALLING ROOT FROM THE TOOLKIT
    obj = Face_Recognition_System(root)             #CREATING AN OBJECT OF CLASS
    root.mainloop()             #CLOSING THE MAIN LOOP 