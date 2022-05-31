from logging import exception
from random import seed
from tkinter import*
from tkinter import ttk   
import tkinter                  
from tkinter import font                 
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
import csv
from tkinter import filedialog

mydata = []

class Attendance :

    def iExit(self) :
            self.iExit = tkinter.messagebox.askyesno("Attendance Management System","Do you Really Want to Exit ?",parent=self.root)
            if self.iExit > 0 :
                self.root.destroy()
            else :
                return

    def __init__(self,root) :           
        self.root = root                   
        self.root.geometry("1410x680+0+0")  
        self.root.title("Attendance Management System") 

        #Variables
        self.var_atten_id = StringVar()
        self.var_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_atten = StringVar()

        #Background Image
        b_img = Image.open(r"images/AttendBg.jpg")          
        b_img = b_img.resize((1410,680),Image.ANTIALIAS)   #Storing the Image into the Variable
        self.b_image = ImageTk.PhotoImage(b_img)  

        bg_image = Label(self.root,image = self.b_image) 
        bg_image.place(x=0,y=0,width=1410,height=680)

        #Time
        def time() :
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(bg_image, font=("Terminal",15,"bold"))
        lbl.place(x=1220,y=100,width=150,height=50)
        time()

        #Creating The Frame In Order To Write Over The Background Image
        main_frame = Frame(bg_image,bd=2)
        main_frame.place(x=5,y=150,width=1355,height=520)

        #Left Side Frame
        left_frame = LabelFrame(main_frame,bd=2,relief=GROOVE,text="Attendance Details",font=("Lucida Sans Unicode",12,"bold"))
        left_frame.place(x=10,y=10,width=655,height=495)

        left_inside_frame = Frame(left_frame,relief=RIDGE,bd=2)
        left_inside_frame.place(x=5,y=5,width=635,height=455)

            #Labels and Entries
        #Attendance Id
        attendance_id_label = Label(left_inside_frame,text="Attendance ID :",font=("Century Gothic",10))
        attendance_id_label.grid(row=0,column=1,padx=10,pady=20,sticky=W)

        attendance_id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("Century Gothic",10))
        attendance_id_entry.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        #Name
        name_label = Label(left_inside_frame,text="Name :",font=("Century Gothic",10))
        name_label.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("Century Gothic",10))
        name_entry.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        #Time
        tim_label = Label(left_inside_frame,text="Time :",font=("Century Gothic",10))
        tim_label.grid(row=0,column=3,padx=5,pady=20,sticky=W)

        tim_entry = ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("Century Gothic",10))
        tim_entry.grid(row=0,column=4,padx=5,pady=15,sticky=W)

        #Date
        date_label = Label(left_inside_frame,text="Date :",font=("Century Gothic",10))
        date_label.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_date,width=20,font=("Century Gothic",10))
        date_entry.grid(row=1,column=4,padx=5,pady=15,sticky=W)

        #Attendance Status
        attendance_label = Label(left_inside_frame,text="Attendance Status",font=("Century Gothic",10))
        attendance_label.grid(row=2,column=1,padx=10)

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten,font=("Century Gothic",10),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=2,column=2,padx=2,pady=15,sticky=W)
        self.atten_status.current(0)                           
        
        #Buttons Label
        btn_lbl_frame = LabelFrame(left_inside_frame,bd=2,relief=GROOVE)
        btn_lbl_frame.place(x=5,y=220,width=620,height=130)

        #Creating Buttons
        save_btn = Button(btn_lbl_frame,text="Import CSV",command=self.importCsv,width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0,padx=10,pady=15)

        update_btn = Button(btn_lbl_frame,text="Export CSV",command=self.exportCsv,width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1,padx=20,pady=15)

        delete_btn = Button(btn_lbl_frame,command=self.iExit,text="Exit",width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        delete_btn.grid(row=1,column=0,padx=20,pady=15)

        reset_btn = Button(btn_lbl_frame,text="Reset",command=self.reset_data,width=20,font=("Terminal",10,"bold"),bg="black",fg="white")
        reset_btn.grid(row=1,column=1,padx=10,pady=15)


        #Right Side Frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=GROOVE,text="Details",font=("Lucida Sans Unicode",12,"bold"))
        Right_frame.place(x=670,y=10,width=665,height=495)

        table_frame = LabelFrame(Right_frame,bd=2,relief=GROOVE)
        table_frame.place(x=5,y=5,width=650,height=455)

        #Scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("ID","Name","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows) :
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows :
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self) :
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread :
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self) :
        try :
            if len(mydata) < 1 :
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile :
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata :
                    exp_write.writerow(i)
                messagebox.showinfo("Export","Data Exported Successfully")
        except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    def get_cursor(self,event="") :
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_time.set(rows[2])
        self.var_date.set(rows[3])
        self.var_atten.set(rows[4])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten.set("")

if __name__ == "__main__":                  
    root = Tk()                                 
    obj = Attendance(root)        
    root.mainloop()     