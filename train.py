from logging import exception
from random import seed
import tkinter
from tkinter import*
from tkinter import ttk                     
from tkinter import font                 
from PIL import Image,ImageTk            
from tkinter import messagebox
import mysql.connector
from mysql.connector.constants import PARAMETER_COUNT_AVAILABLE
from mysql.connector.errors import DatabaseError
import cv2
import os
import numpy as np

class Train :

    def iExit(self) :
            self.iExit = tkinter.messagebox.askyesno("Data Indoctrination","Do you Really Want to Exit ?",parent=self.root)
            if self.iExit > 0 :
                self.root.destroy()
            else :
                return
    
    def __init__(self,root) :           
        self.root = root                   
        self.root.geometry("1410x680+0+0")  
        self.root.title("Data Indoctrination")        

        #Background Image
        b_img = Image.open(r"images/TrainData.jpg")          
        b_img = b_img.resize((1410,680),Image.ANTIALIAS)   #Storing the Image into the Variable
        self.b_image = ImageTk.PhotoImage(b_img)  

        bg_image = Label(self.root,image = self.b_image) 
        bg_image.place(x=0,y=0,width=1410,height=680) 
        
        #Exit Button
        b1 = Button(bg_image,text="Exit",command=self.iExit,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b1.place(x=10,y=50,width=160,height=30)
        #Train Data button
        b2 = Button(bg_image,text="Start",command=self.train_classifier,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b2.place(x=520,y=480,width=300,height=40)


    def train_classifier(self):
        data_dir = ("data/")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces = []
        ids = []

        for image in path :
            img = Image.open(image).convert('L') #Converting image into gray scale image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)

            ids.append(id)
            
            cv2.imshow("Indoctrination",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        #Indoctrination of Classifier and Saving
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)

        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Done","Data Indoctrination Complete")


if __name__ == "__main__":                  
    root = Tk()                                 
    obj = Train(root)             
    root.mainloop()             