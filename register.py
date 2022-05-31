from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register :
    def __init__(self,root) :
        self.root = root
        self.root.title("Create New User")
        self.root.geometry("800x600+50+50")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        frame = Frame(self.root)
        frame.place(x=0,y=0,width=800,height=600)

        register_lbl = Label(frame,text="Register Here",font=("Times New Roman",20,"bold"),fg="Black")
        register_lbl.place(x=20,y=20)


        fname = Label(frame,text="First Name",font=("Times New Roman",15,"bold"))
        fname.place(x=50,y=100)

        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("Times New Roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame,text="Last Name",font=("Times New Roman",15,"bold"))
        lname.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("Times New Roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        contact = Label(frame,text="Contact",font=("Times New Roman",15,"bold"))
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("Times New Roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text="E-mail",font=("Times New Roman",15,"bold"))
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("Times New Roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        security_q = Label(frame,text="Security Question",font=("Times New Roman",15,"bold"))
        security_q.place(x=50,y=240)

        self.combo_security_q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Times New Roman",15,"bold"),state="readonly")
        self.combo_security_q["values"] = ("Select","What is your Birthdate","What is your Pet Name","Your Collage Name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a = Label(frame,text="Security Answer",font=("Times New Roman",15,"bold"))
        security_a.place(x=370,y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA,font=("Times New Roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        pswd = Label(frame,text="Password",font=("Times New Roman",15,"bold"))
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("Times New Roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd = Label(frame,text="Confirm Password",font=("Times New Roman",15,"bold"))
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("Times New Roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        registerbtn = Button(frame,text="Register",command=self.register_data,font=("Terminal",12,"bold"),bd=3,relief=RIDGE,fg="White",bg="Black")
        registerbtn.place(x=50,y=420,width=230,height=45)

        loginnowbtn = Button(frame,text="Login Now",font=("Terminal",12,"bold"),bd=3,relief=RIDGE,fg="White",bg="Black")
        loginnowbtn.place(x=370,y=420,width=230,height=45)


    def register_data(self) :
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" :
            messagebox.showerror("Warrning","Required All Fields")
        elif self.var_pass.get() != self.var_confpass.get() :
            messagebox.showerror("Error","Password and Confirm Password Should be Same")
        else :
            conn = mysql.connector.connect(host = "localhost", user = "root", password ="", database = "face_recognizer")
            mycursor = conn.cursor()
            query = ("Select * from register where email=%s")
            value = (self.var_email.get(),)
            mycursor.execute(query,value)
            row = mycursor.fetchone()
            if row != None :
                messagebox.showerror("Error","E-mail is Already Registered")
            else :
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Register Successfully")


if __name__ == "__main__" :
    root = Tk()
    app = Register(root)
    root.mainloop()