from logging import exception
from random import seed
from tkinter import*
import tkinter
from tkinter import ttk                     
from tkinter import font                 
from PIL import Image,ImageTk            
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
from mysql.connector.constants import PARAMETER_COUNT_AVAILABLE
from mysql.connector.errors import DatabaseError
import cv2

class Student :   

    def iExit(self) :
            self.iExit = tkinter.messagebox.askyesno("Student Management System","Do you Really Want to Exit ?",parent=self.root)
            if self.iExit > 0 :
                self.root.destroy()
            else :
                return  

    #Making the Function to Add the Functionality to the Buttons
    def add_data(self) : 
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else :
            try :
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()       #Creating Cursor In Order To Execute The MYSQL Query
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dept.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_mobile.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Done!","Record has been stored Successfully",parent=self.root)    
            except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #Fetching the Data
    def fetch_data(self) :
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0 :
            self.stud_table.delete(*self.stud_table.get_children())
            for i in data :
                self.stud_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Creating Function To Take The Data From Display Data Section In Order To Update It
    def get_cursor(self,event=""):
        cursor_focus = self.stud_table.focus()
        content = self.stud_table.item(cursor_focus)
        data = content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_mobile.set(data[8]),
        self.var_email.set(data[9]),
        self.var_address.set(data[10]),
        self.var_gender.set(data[11]),
        self.var_radio1.set(data[12])

        #Update Function
    def upadate_data(self) :
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else :
            try :
                upadate = messagebox.askyesno("Are you Sure ?","Do you Want to Update this Record ?",parent=self.root)
                if upadate > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set `Department`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`Name`=%s,`Division`=%s,`D.O.B`=%s,`Mobile`=%s,`E-mail`=%s,`Address`=%s,`Gender`=%s,`Photo`=%s where `Id`=%s",(
                                                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_radio1.get(),  
                                                                                                                                                                                                self.var_id.get()
                                                                                                                                                                                            ))
                else :
                    if not upadate :
                        return
                messagebox.showinfo("Done !","Record is Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    #Delete funtion
    def delete_data(self) :
        if self.var_id.get() == "" :
            messagebox.showerror("Error","Student I.D Required",parent=self.root)
        else :
            try :
                delete = messagebox.askyesno("Delete !","Are you Sure you want to Delete this Record",parent=self.root)
                if delete > 0 :
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from student where `Id`=%s",(
                                                                    self.var_id.get(),
                                                                ))
                else :
                    if not delete :
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Record Deleted Successfully",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    #Reset Function
    def reset_data(self) :
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_dob.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_gender.set("")
        self.var_radio1.set("")



    #Generate DataSet and Take the Sample Photo And Store the  X100 Photo In Data Folder
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" :
            messagebox.showerror("Error","All Feilds are Required",parent=self.root)
        else:
            try :
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult :
                    id+=1
                my_cursor.execute("update student set `Department`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`Name`=%s,`Division`=%s,`D.O.B`=%s,`Mobile`=%s,`E-mail`=%s,`Address`=%s,`Gender`=%s,`Photo`=%s where `Id`=%s",(
                                                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_radio1.get(),  
                                                                                                                                                                                                self.var_id.get()==id+1
                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                                        #Load Predefined Data On Face Frontal Data From Opencv Haarcasade
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
                def face_cropped(img) :
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) 
                    #Scalling Factor = 1.1 
                    #Minimum Neighbour = 4
                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                    #Detecting Eye
                    eyes=eye_classifier.detectMultiScale(gray)
                    for (ex,ey,ew,eh) in eyes :
                        cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                #Opening The Camera
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None :
                        img_id+=1
                        # Resizeing the Image in Order to Save the Cropped Face Image
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Scanning Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100 :
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Compeleted",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)




    def __init__(self,root) :           
        self.root = root                   
        self.root.geometry("1410x680+0+0")  
        self.root.title("Face Recognition System")     
   

        #Variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_dob = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        #Background Image
        b_img = Image.open(r"images/SMS.png")        
        b_img = b_img.resize((1410,680),Image.ANTIALIAS)   
        self.b_image = ImageTk.PhotoImage(b_img)  
    
        bg_image = Label(self.root,image = self.b_image) 
        bg_image.place(x=0,y=0,width=1410,height=680)

        #Time
        def time() :
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(bg_image, font=("Terminal",15,"bold"))
        lbl.place(x=1220,y=140,width=150,height=50)
        time()

        #Creating The Frame In Order To Write Over The Background Image
        main_frame = Frame(bg_image,bd=2)
        main_frame.place(x=5,y=180,width=1355,height=490)

        #LEFT LABEL FRAME
        left_frame = LabelFrame(main_frame,bd=2,relief=GROOVE,text="Student Details",font=("Lucida Sans Unicode",12,"bold"))
        left_frame.place(x=10,y=10,width=655,height=475)

        #Current Course Label
        cc_lbl_frame = LabelFrame(left_frame,bd=2,relief=GROOVE,text="Current Course Infromation",font=("Franklin Gothic",12,"bold"))
        cc_lbl_frame.place(x=5,y=10,width=645,height=130)

        #Department Label
        dept_label = Label(cc_lbl_frame,text="Department",font=("Century Gothic",10))
        dept_label.grid(row=0,column=0,padx=10)

        #Making the Combo Box
        dept_combo = ttk.Combobox(cc_lbl_frame,textvariable=self.var_dept,font=("Century Gothic",10),state="readonly")

        #Inserting the Values in the ComboBox by using Tupple
        dept_combo["values"]=("Select Department","Civil","Financal","I.T","Engineering","Business")
        dept_combo.current(0)                           #Showing the Current Selected Before Making a Choice
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course Label
        dept_label = Label(cc_lbl_frame,text="Course",font=("Century Gothic",10))
        dept_label.grid(row=0,column=2,padx=10)

        dept_combo = ttk.Combobox(cc_lbl_frame,textvariable=self.var_course,font=("Century Gothic",10),state="readonly")
        dept_combo["values"]=("Select Course","B.Com","B.Ed","BCA","M.Com","B.Tech")
        dept_combo.current(0)                           
        dept_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year Label
        dept_label = Label(cc_lbl_frame,text="Year",font=("Century Gothic",10))
        dept_label.grid(row=1,column=0,padx=10)

        dept_combo = ttk.Combobox(cc_lbl_frame,textvariable=self.var_year,font=("Century Gothic",10),state="readonly")
        dept_combo["values"]=("Select Year","2017-2018","2019-2020","2021-2022","2023-2024")
        dept_combo.current(0)                           
        dept_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester Label
        dept_label = Label(cc_lbl_frame,text="Semester",font=("Century Gothic",10))
        dept_label.grid(row=1,column=2,padx=10)

        dept_combo = ttk.Combobox(cc_lbl_frame,textvariable=self.var_sem,font=("Century Gothic",10),state="readonly")
        dept_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        dept_combo.current(0)                           
        dept_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student Information Label
        stud_info_frame = LabelFrame(left_frame,bd=2,relief=GROOVE,text="Student Infromation",font=("Franklin Gothic",12,"bold"))
        stud_info_frame.place(x=5,y=140,width=640,height=300)
        
        #StudentId
        stud_id_label = Label(stud_info_frame,text="Student ID",font=("Century Gothic",10))
        stud_id_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stud_id_entry = ttk.Entry(stud_info_frame,textvariable=self.var_id,width=20,font=("Century Gothic",10))
        stud_id_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Studentname
        stud_name_label = Label(stud_info_frame,text="Student Name",font=("Century Gothic",10))
        stud_name_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stud_name_entry = ttk.Entry(stud_info_frame,textvariable=self.var_name,width=20,font=("Century Gothic",10))
        stud_name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Division
        stud_div_label = Label(stud_info_frame,text="Division",font=("Century Gothic",10))
        stud_div_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        stud_div_entry = ttk.Entry(stud_info_frame,textvariable=self.var_div,width=20,font=("Century Gothic",10))
        stud_div_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Student Date of Birth
        stud_dob_label = Label(stud_info_frame,text="D.O.B",font=("Century Gothic",10))
        stud_dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        stud_dob_entry = ttk.Entry(stud_info_frame,textvariable=self.var_dob,width=20,font=("Century Gothic",10))
        stud_dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Student Mobile
        stud_phone_label = Label(stud_info_frame,text="Mobile",font=("Century Gothic",10))
        stud_phone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        stud_phone_entry = ttk.Entry(stud_info_frame,textvariable=self.var_mobile,width=20,font=("Century Gothic",10))
        stud_phone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Student Email
        stud_mail_label = Label(stud_info_frame,text="E-mail",font=("Century Gothic",10))
        stud_mail_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        stud_mail_entry = ttk.Entry(stud_info_frame,textvariable=self.var_email,width=20,font=("Century Gothic",10))
        stud_mail_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Student Address
        stud_address_label = Label(stud_info_frame,text="Address",font=("Century Gothic",10))
        stud_address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stud_address_entry = ttk.Entry(stud_info_frame,textvariable=self.var_address,width=20,font=("Century Gothic",10))
        stud_address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Student Gender
        stud_mail_label = Label(stud_info_frame,text="Gender",font=("Century Gothic",10))
        stud_mail_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        self.var_gender=StringVar()
        stud_gender_label = ttk.Radiobutton(stud_info_frame,variable=self.var_gender,text="Male",value="Male")
        stud_gender_label.grid(row=3,column=3,padx=0,pady=5,sticky=W)

        gender_entry = ttk.Radiobutton(stud_info_frame,variable=self.var_gender,text="Female",value="Female")
        gender_entry.grid(row=4,column=3,padx=0,pady=5,sticky=W)

        #Creating the Radio Button
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(stud_info_frame,variable=self.var_radio1,text="Take a Photo",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        radiobtn2 = ttk.Radiobutton(stud_info_frame,variable=self.var_radio1,text="Don't Take Photo",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=5,sticky=W)


        #Buttons Label
        btn_lbl_frame = LabelFrame(left_frame,bd=2,relief=GROOVE)
        btn_lbl_frame.place(x=10,y=360,width=630,height=75)

        #Creating Buttons
        save_btn = Button(btn_lbl_frame,command=self.add_data,text="Save",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=2)

        update_btn = Button(btn_lbl_frame,command=self.upadate_data,text="Update",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=2)

        delete_btn = Button(btn_lbl_frame,command=self.delete_data,text="Delete",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=2)

        reset_btn = Button(btn_lbl_frame,command=self.reset_data,text="Reset",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        reset_btn.grid(row=1,column=0,padx=5,pady=2)

        tak_pic_btn = Button(btn_lbl_frame,command=self.generate_dataset,text="Take Photo",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        tak_pic_btn.grid(row=1,column=1,padx=5,pady=2)

        up_btn = Button(btn_lbl_frame,command=self.iExit,text="Exit",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        up_btn.grid(row=1,column=2,padx=5,pady=2)

        #RIGHT LABEL FRAME
        Right_frame = LabelFrame(main_frame,bd=2,relief=GROOVE,text="Student Details",font=("Lucida Sans Unicode",12,"bold"))
        Right_frame.place(x=670,y=10,width=665,height=475)

        #Search Frame
        Search_frame = LabelFrame(Right_frame,bd=2,relief=GROOVE,text="Search",font=("Franklin Gothic",12,"bold"))
        Search_frame.place(x=5,y=10,width=640,height=75)

        #Griding the Label 
        search_label = Label(Search_frame,text="Filters",font=("System",15))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)  

        search_combo = ttk.Combobox(Search_frame,font=("Century Gothic",10),state="readonly")
        search_combo["values"]=("Select","I.D","Mobile","Name","E-mail")
        search_combo.current(0)                           
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Entery Feild to take the Data
        search_entry = ttk.Entry(Search_frame,width=20,font=("Century Gothic",10))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search Button
        search_btn = Button(Search_frame,text="Search",width=5,font=("Terminal",10,"bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        #Display All Button
        show_btn = Button(Search_frame,text="Display",width=5,font=("Terminal",10,"bold"),bg="black",fg="white")
        show_btn.grid(row=0,column=4,padx=5)

        #Creating Table Frame
        Table_frame = Frame(Right_frame,bd=2,relief=GROOVE)
        Table_frame.place(x=5,y=90,width=645,height=350)

        #Scroll bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        #Creating Tree View 
        self.stud_table = ttk.Treeview(Table_frame,column=("Department","Course","Year","Semester","I.D","Name","Division","D.O.B","Mobile","E-mail","Address","Gender","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        #Configuring the Scroll bar
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("Department",text="Department")
        self.stud_table.heading("Course",text="Course")
        self.stud_table.heading("Year",text="Year")
        self.stud_table.heading("Semester",text="Semester")
        self.stud_table.heading("I.D",text="I.D")
        self.stud_table.heading("Name",text="Name")
        self.stud_table.heading("Division",text="Division")
        self.stud_table.heading("D.O.B",text="D.O.B")
        self.stud_table.heading("Mobile",text="Mobile")
        self.stud_table.heading("E-mail",text="E-mail")
        self.stud_table.heading("Address",text="Address")
        self.stud_table.heading("Gender",text="Gender")
        self.stud_table.heading("Photo",text="Photo")

        self.stud_table["show"]="headings"

        #Setting the Width of the Columns
        self.stud_table.column("Department",width=100)
        self.stud_table.column("Course",width=100)
        self.stud_table.column("Year",width=100)
        self.stud_table.column("Semester",width=100)
        self.stud_table.column("I.D",width=100)
        self.stud_table.column("Name",width=100)
        self.stud_table.column("Division",width=100)
        self.stud_table.column("D.O.B",width=100)
        self.stud_table.column("Mobile",width=100)
        self.stud_table.column("E-mail",width=100)
        self.stud_table.column("Address",width=100)
        self.stud_table.column("Gender",width=100)
        self.stud_table.column("Photo",width=100)


        self.stud_table.pack(fill=BOTH,expand=1)
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



if __name__ == "__main__":                  
    root = Tk()                                 
    obj = Student(root)             