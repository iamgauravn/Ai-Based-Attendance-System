from logging import exception
from random import seed
from tkinter import*
from tkinter import ttk                     
from tkinter import font  
import tkinter               
from PIL import Image,ImageTk            
from tkinter import messagebox
import mysql.connector
from mysql.connector.constants import PARAMETER_COUNT_AVAILABLE
from mysql.connector.errors import DatabaseError
import cv2
from datetime import datetime
from time import strftime
import os
import numpy as np

class Face_Recognition :

    def iExit(self) :
            self.iExit = tkinter.messagebox.askyesno("Take Attendance","Do you Really Want to Exit ?",parent=self.root)
            if self.iExit > 0 :
                self.root.destroy()
            else :
                return

    def __init__(self,root) :           
        self.root = root                   
        self.root.geometry("1410x680+0+0")  
        self.root.title("Take Attendance")        

        #Background Image
        b_img = Image.open(r"images/Face.png")          
        b_img = b_img.resize((1410,680),Image.ANTIALIAS)   #Storing the Image into the Variable
        self.b_image = ImageTk.PhotoImage(b_img)  

        bg_image = Label(self.root,image = self.b_image) 
        bg_image.place(x=0,y=0,width=1410,height=680) 
        
        #Exit Button
        b2 = Button(bg_image,text="Exit",command=self.iExit,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b2.place(x=10,y=50,width=200,height=30)
        #Face Detect button
        b2 = Button(bg_image,text="WebCam",command=self.face_recog,cursor="hand2",font=("Terminal",15,"bold"),bg="black",fg="white")
        b2.place(x=830,y=390,width=300,height=40)

    #Taking Attendance
    def mark_attendance(self,my_id,my_id2) :
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            
            for line in myDataList :
                entry = line.split((","))
                name_list.append(entry[0])
            
            if((my_id not in name_list) and (my_id2 not in name_list)) :
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{my_id},{my_id2},{dtString},{d1},Present")

    #Face Recognition
    def face_recog(self) :
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf) :
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]
            
            for (x,y,w,h) in features :
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])

                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("Select Name from student where Id="+str(id))
                n = my_cursor.fetchone()
                #n="+".join(n)
                separator=''
                my_id=separator.join(str(id)for id in n)

                my_cursor.execute("Select Id from student where Id="+str(id))
                j = my_cursor.fetchone()
                #j="+".join(j)
                separator=''
                my_id2=separator.join(str(id)for id in j)

                if confidence > 78 :
                    cv2.putText(img, f"Name :{my_id}", (x,y-44), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Id :{my_id2}", (x,y-0), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    self.mark_attendance(my_id, my_id2)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Person", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)

                coord = [x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade) :
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True :
            ret,img = video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("WebCam",img)
            
            if cv2.waitKey(1) == 13 :
                break
            
        video_cap.release()
        cv2.destroyAllWindows()
        video_cap.release()

if __name__ == "__main__":                  
    root = Tk()                                 
    obj = Face_Recognition(root)             
    root.mainloop()             