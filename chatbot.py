from tkinter import*
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

class ChatBot :
    def __init__(self,root) :
        self.root = root
        self.root.title("Chat Bot")
        self.root.geometry("730x580+0+0")
        self.root.bind('<Return>',self.enter_fun)

        main_frame = Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=65,height=20,border=3,relief=RAISED,font=('Terminal',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side = RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame,text="Ask Me",font=('Terminal',14,'bold'),bg='black',fg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('Times New Roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send = Button(btn_frame,command=self.send,text="Send",font=('Terminal',14,'bold'),width=8,bg='powder blue')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear = Button(btn_frame,command=self.clear,text="Clear",font=('Terminal',14,'bold'),width=8,bg='gray')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame,text=self.msg,font=('Terminal',14,'bold'),bg='black',fg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

    def enter_fun(self,event) :
        self.send.invoke()
        self.entry.set('')

    def clear(self) :
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self) :
        send = 'You : ' +self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get() == '') :
            self.msg = 'PLease Enter Some Input'
            self.label_11.config(text=self.msg,fg='red',bg='white')
        else :
            self.msg = ''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get() == 'hi') :
            self.text.insert(END, '\n\n' + 'Bot : Hello')

        elif(self.entry.get() == 'hello') :
            self.text.insert(END, '\n\n' + 'Bot : Hi')

        elif(self.entry.get() == 'help') :
            self.text.insert(END, '\n\n' + 'Bot : Hello There ! How May I Help You')

        elif(self.entry.get() == 'Options') :
            self.text.insert(END, '\n\n\t' + 'Bot : Who are you ?\n\tLanguage\n\tAlgorithm\n\tCreator\n\t\n\tDo you Feel Anything ?\n\tAre you a Human ?\n\tE-mail\n\tHow to take Attendance?\n\t')

        elif(self.entry.get() == 'Who are you ?') :
            self.text.insert(END, '\n\n' + "Bot : I'm you're Little Assistant and I'm here to Help you Anything you want you just have to ask me for it")

        elif(self.entry.get() == 'Are you a Human ?') :
            self.text.insert(END, '\n\n' + "Bot : I'm Afraid Not I am Just a Robot Made Up of Python Script")

        elif(self.entry.get() == 'Do you Feel Anything ?') :
            self.text.insert(END, '\n\n' "Bot : Since I'm a Bot I Don't Feel Anything But I'm sure I can help you with you're problem")

        elif(self.entry.get() == 'E-mail') :
            self.text.insert(END, '\n\n' + 'Bot : \tnishanttrivedi474@gmail.com \n\thearmegaurav@gmail.com')

        elif(self.entry.get() == 'Language') :
            self.text.insert(END, '\n\n' + 'Bot : Python Language')

        elif(self.entry.get() == 'Creator') :
            self.text.insert(END, '\n\n' + 'Bot : Gaurav Nandankar And Nishant Trivedi')

        elif(self.entry.get() == 'Algorithm') :
            self.text.insert(END, '\n\n' + 'Bot : Haarcascade and LBPH (Local Binary Pattern Histogram)')

        elif (self.entry.get() == 'How to take Attendance?'):
            self.text.insert(END, '\n\n' + 'Bot : In order to take Attendance , you have to follow \nsome steps \n\nStep 1 :- Go to Student Management System and Insert your all \ninformation\n\nStep 2 :- Go to Train Data Option it will train your photo \nusing (Haar cascade and LBPH Algorithm) \n\nSter 3 :- Go to Take Attendance option and CLick on "Webcam" \nNow a window will appear there and capture your face \n(It will match your Real time Face with available Students \nPhotos)\n\n\n You did it !!')

        else :
            self.text.insert(END, '\n\n' + "Bot : Sorry I Didn't Get That")

if __name__ == '__main__' :
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()