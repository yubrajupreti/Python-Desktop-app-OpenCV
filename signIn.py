import os
from tkinter import *
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox


import sqlite3

class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("HITO")
        self.root.geometry("1350x700+0+0")

        # title of the window defined
        title = Label(self.root, text="Create Account", font=("times new roman", 40, "bold"), bg="green", fg="yellow", bd=10,
                      relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # frame defined
        Login_frame = Frame(self.root, bg="white")
        Login_frame.place(x=400, y=100)

        # variable defined for user-input box
        self.name=StringVar()
        self.address = StringVar()
        self.phone = IntVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.re_password = StringVar()

        # info with box is defind for user input

        # name info
        name_label = Label(Login_frame, text="Name",justify=LEFT,anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20)
        # name input
        name_entry = Entry(Login_frame, bd=5, textvariable=self.name, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20, pady=10)

        # address info
        address_label = Label(Login_frame, text="Address", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=3, column=0)
        # adress input
        address_entry = Entry(Login_frame, bd=5, textvariable=self.address,  relief=GROOVE,
                               font=("", 15)).grid(row=3, column=1, padx=20, pady=10)

        # phone info
        phone_label = Label(Login_frame, text="Phone", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=4, column=0)
        # phone input
        phone_entry = Entry(Login_frame, bd=5, textvariable=self.phone, relief=GROOVE,
                               font=("", 15)).grid(row=4, column=1, padx=20, pady=10)

        # email info
        Email_label = Label(Login_frame, text="Email", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=5, column=0)
        # email input
        Email_entry = Entry(Login_frame, bd=5, textvariable=self.email, relief=GROOVE,
                               font=("", 15)).grid(row=5, column=1, padx=20, pady=10)

        # dob info
        dob = Label(Login_frame, text="Date of Birth", justify=LEFT, anchor=SW,
                    font=("times new roman", 20, "bold")).grid(row=6, column=0, padx=5)
        # dob input
        dob_cal = DateEntry(Login_frame, width=18, textvariable=self.dob, year=2010, font=("", 15, "bold")).grid(row=6, column=1, padx=5)

        # username info
        Username_label = Label(Login_frame, text="Username", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=7, column=0)
        # username inout
        Username_entry = Entry(Login_frame, bd=5,  relief=GROOVE, textvariable=self.username,
                               font=("", 15)).grid(row=7, column=1, padx=20, pady=10)

        # password info
        password_label = Label(Login_frame, text="Password", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=8, column=0)
        # password input
        password_entry = Entry(Login_frame, bd=5, show="*", relief=GROOVE, textvariable=self.password,
                               font=("", 15)).grid(row=8, column=1, padx=20, pady=10)

        # password re-input info
        confirm_label = Label(Login_frame, text="Re-Password", justify=LEFT, anchor=SW,
                               font=("times new roman", 20, "bold")).grid(row=9, column=0,padx=5)
        # password re-input
        confirm_entry = Entry(Login_frame, bd=5, show="*", relief=GROOVE,  textvariable=self.re_password,
                               font=("", 15)).grid(row=9, column=1, padx=20, pady=10)
        # info who has account
        info = Label(Login_frame, text="Already have an account.", justify=LEFT, anchor=SW,
                              font=("times new roman", 14, "bold")).grid(row=11, column=0, padx=5)

        sign_button=Button(Login_frame,text="Continue",command=self.creatAccount, width=10,font=("times new roman",14,"bold"),bg="green",fg="black").grid(row=10,column=1,pady=10)

        login_button=Button(Login_frame,text="LogIn",command=self.back, width=10,font=("times new roman",14,"bold"),bg="green",fg="black").grid(row=12,column=0,pady=10,padx=10)

    # action method of login_button
    def back(self):
        self.root.destroy()
        os.system('python login.py')


    # action method of signIn_button
    def creatAccount(self):

        # database connectivity
        conn = sqlite3.connect("hito_login.db")
        c = conn.cursor()

        c.execute("SELECT username,email FROM User ")
        data1 = c.fetchall()
        print(data1)

        # variable declared for user input storing
        username=self.username.get()

        email=self.email.get()
        password=self.password.get()
        re_password=self.re_password.get()
        name=self.name.get()

        try:
            phone=self.phone.get()
        except:
            messagebox.showerror("Error", "Invalid Input")

        dob=self.dob.get()
        address=self.address.get()

        flag=True
        while True:
            # email validation
            if email == "":
                flag=False
                messagebox.showerror("Error", "Email Field cannot be blank")
                break

            for u_email in data1:
                # removing bracket for comparing
                existing_email = ''.join(u_email[1])

                # comparing
                if existing_email == email:
                    flag=False
                    messagebox.showerror("Error","The email is already register in the system. Please login or provide another email ")
                    break


            # username validation
            if username == "":
                flag=False
                messagebox.showerror("Error", "Username Field cannot be blank")
                break


            for u_name in data1:
                existing_username = ''.join(u_name[0])
                if existing_username == username:
                    flag=False
                    messagebox.showerror("Error","The username is already taken. Please choose another ")
                    break

            # phone number validation
            str_phone = str(phone)
            if len(str_phone) != 10:
                flag = False
                messagebox.showerror("Error", "Please! Provide valid phone number")
                break

            if phone == "":
                flag = False
                messagebox.showerror("Error", "Please! Phone field cannot be empty")
                break

            # password validation
            if password == "":
                flag = False
                messagebox.showerror("Error", "Password Field cannot be blank")
                break

            # password length validation
            if len(password) < 8:
                flag = False
                messagebox.showerror("Error","Password shoul be combination of 8 character")
                break

            # password confirmation
            if password!=re_password:
                flag = False
                messagebox.showerror("Error", "Password doesnot match")
                break

            break



        if flag==True:
            self.root.destroy()
            # inserting the data into database
            c.execute("INSERT INTO User  VALUES(?,?,?,?,?,? )", (name, email, phone, username, address, password))

            conn.commit()
            os.system(' python face_sigin.py')


root=Tk()
obj=Login(root)
root.mainloop()
