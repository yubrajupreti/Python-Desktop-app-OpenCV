from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os




import sqlite3


active_user=''
class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("HITO")
        self.root.geometry("1350x700+0+0")
        self.root.bind('<Return>', self.login_user)

        #resizing the face image
        self.face = Image.open("Photo/user_photo.png")
        self.user=Image.open("Photo/user.png")
        self.password=Image.open("Photo/password.png")

        self.resize_face = self.face.resize((100, 100), Image.ANTIALIAS)
        self.resize_user=self.user.resize((20, 20), Image.ANTIALIAS)
        self.resize_password = self.password.resize((20, 20), Image.ANTIALIAS)

        #importing image
        self.bg_icon=ImageTk.PhotoImage(file="Photo/bk.jpg")
        self.user_icon=ImageTk.PhotoImage(self.resize_user)
        self.password_icon=ImageTk.PhotoImage(self.resize_password)
        self.face_icon=ImageTk.PhotoImage(self.resize_face)

        self.username=StringVar()
        self.pass_word=StringVar()

        # title of the project
        title = Label(self.root, text="Hito", font=("times new roman", 40, "bold"), bg="green", fg="yellow", bd=10,
                      relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        #defining frame for login
        Login_frame=Frame(self.root, bg="white")
        Login_frame.place(x=400,y=150)

        #displaying the face image which act as button
        self.face_logo = Button(Login_frame, image=self.face_icon,command=self.face_access)
        self.face_logo.grid(row=0, columnspan=2, pady=10)

        # hover effect for user instruction
        self.face_hover=Label(Login_frame,text="")
        self.face_hover.grid(row=1, columnspan=2,pady=10)
        self.face_logo.bind("<Enter>",self.hover)
        self.face_logo.bind("<Leave>", self.hover_left)

        # username field
        user_label=Label(Login_frame,text="Username", image=self.user_icon,compound=LEFT,
                   font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20)
        user_entry=Entry(Login_frame,bd=5,textvariable=self.username,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        # password field
        password_label = Label(Login_frame, text="Password", image=self.password_icon, compound=LEFT,
                     font=("times new roman", 20, "bold")).grid(row=3, column=0, padx=10)
        password_entry = Entry(Login_frame, bd=5,textvariable=self.pass_word,show="*", relief=GROOVE, font=("", 15)).grid(row=3, column=1, padx=20,pady=10)

        # button defined with action
        login_button=Button(Login_frame,text="Login",command=self.login_user, width=15,font=("times new roman",14,"bold"),bg="blue",fg="black").grid(row=4,column=1,pady=10)
        SignIn_button=Button(Login_frame,text="SignIn",command=self.signIn, width=8,font=("times new roman",14,"bold"),bg="Grey",fg="black").grid(row=0,column=3,pady=50)

    # action method of button face
    def face_access(self):
        # calling another file to execute
        os.system('python unknown_webcamp.py')

    # hover method
    def hover(self,event):
        self.face_hover.configure(text="Click to Login through Face")

    # hover method
    def hover_left(self,event):
        self.face_hover.configure(text="")

    # action method for creating new user
    def signIn(self):

        # closing the open window
        self.root.destroy()
        os.system(' python signIn.py')


    # login method for user validation
    def login_user(self,event=None):

        # database connectivity
        conn = sqlite3.connect("hito_login.db")
        c = conn.cursor()
        c.execute("SELECT username,password FROM User")
        users = c.fetchall()
        print(users)

        # while True:

        user_flag = False

        # loop for user validation
        for user in users:
            if user[0] == self.username.get() and user[1] == self.pass_word.get():
                global active_user
                active_user=self.username.get()
                print(active_user)

                user_flag = True
                # print("match found")
                break

        if user_flag == False:
            messagebox.showerror("Error","Either username or password is incorrect")
            # if msg=="ok":
            #     messagebox.showerror.destroy()

        elif user_flag==True:
            self.root.destroy()
            os.system('python home.py')
            # messagebox.showinfo("Successful","You are logged in ")
        else:
            messagebox.showerror("Error","Invalid Input")



#
# print(active_user)

root=Tk()
obj=Login(root)
print(obj)
# obj.inital(root)
root.mainloop()





