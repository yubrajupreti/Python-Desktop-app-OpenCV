import os
from tkinter import *

import cv2
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

# database connection
conn = sqlite3.connect('hito_login.db')
c=conn.cursor()

class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("HITO")
        self.root.geometry("1350x700+0+0")

        # title of the page is defined
        title = Label(self.root, text="Face Conformation", font=("times new roman", 40, "bold"), bg="green", fg="yellow", bd=10,
                      relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # frame is defined in a window
        self.Login_frame = Frame(self.root, bg="white")
        self.Login_frame.place(x=400, y=100)

        # variable name defined for userinput box
        self.username=StringVar()

        # opening the image file
        self.face = Image.open("Photo/user_photo.png")
        self.user = Image.open("Photo/user.png")

        # reseizing the image
        self.resize_face = self.face.resize((300, 300), Image.ANTIALIAS)
        self.resize_user = self.user.resize((20, 20), Image.ANTIALIAS)

        # loading in tkinter
        self.face_icon = ImageTk.PhotoImage(self.resize_face)
        self.user_icon = ImageTk.PhotoImage(self.resize_user)

        # placing the image
        self.face_logo = Label(self.Login_frame, image=self.face_icon)
        self.face_logo.grid(row=0, column=0, pady=10)

        # button defined with action
        click = Button(self.Login_frame, text="Click",  width=15, command=self.upload,
                             font=("times new roman", 14, "bold"), bg="blue", fg="black").grid(row=1, column=0)

        # user guideline text is definedinput box defined
        user_label = Label(self.Login_frame, text="Enter your username to confirm.", image=self.user_icon, compound=LEFT,
                           font=("times new roman", 16, "bold")).grid(row=3, column=0, pady=10)

        # user input box is defined
        user_entry = Entry(self.Login_frame, bd=5,textvariable=self.username,  relief=GROOVE, font=("", 15)).grid(row=4,column=0,padx=20)

        set = Button(self.Login_frame, text="SET", width=15, command=self.save,
                       font=("times new roman", 14, "bold"), bg="blue", fg="black").grid(row=5, column=0,pady=20)


    # action method of button click
    def upload(self):
        os.system('python known_webcamp.py')

        # converting normal image into binary form
        def convertToBinaryData(filename):

            # Convert digital data to binary format
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData

        # nested method for clicking user photo by accesing webcamp and storing in folder
        def webcamp():


            # Open the device at the ID 0
            cap = cv2.VideoCapture(0)

            # counter variable for clicking number of photo
            i = 0

            while i < 1:

                path = f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Access_photo'

                return_value, image = cap.read()

                # image store in the given path
                cv2.imwrite(os.path.join(path, 'first' + '.jpg'), image)
                i += 1

                # the returned data from method is saved in self.photo
                self.photo = convertToBinaryData(
                    f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Access_photo/first.jpg')


                # counter variable increament
                i += 1

                # Waits for a user input to quit the application

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # When everything done, release the capture
            # del (cap)
            cap.release()
            # out.release()
            # cv2.destroyWindows('preview')
            cv2.waitKey(100000)

        # calling methods
        webcamp()

        self.face = Image.open("Access_photo/first.jpg")
        self.resize_face = self.face.resize((300, 300), Image.ANTIALIAS)

        self.face_icon = ImageTk.PhotoImage(self.resize_face)

        self.face_logo = Label(self.Login_frame, image=self.face_icon)
        self.face_logo.grid(row=0, column=0, pady=10)


    # action method of button set
    def save(self):

        # username enterd by user is stored in username variable
        username=self.username.get()

        # sql command
        c.execute("SELECT username from User")

        # all data are store in all_name
        all_name = c.fetchall()
        flag = False

        while True:
            # for loop for checking valid username
            for name in all_name:
                existing_name = ''.join(name)

                if username == existing_name:
                    flag = True

            # un-valid user message
            if flag==False:
                messagebox.showerror("Error", "Username doesnot exist.")
                break

            # if user is valid
            else:
                c.execute("SELECT username from Known_face")
                face_name = c.fetchall()

                # boolen value to determine the user info
                bool = True

                # for loop for checking the given username has face recognation services or not
                for f_name in face_name:
                    existing_face_name = ''.join(f_name)

                    # if provided username has already activate face detection
                    if username == existing_face_name:

                        messagebox.showerror("Error","The username has already face detection ")
                        # if msg=='ok':
                        #     messagebox.showerror.destroy()
                        bool = False
                        break

                if bool == False:
                    break

                # if user doesnot have face recognization facility
                else:
                    c.execute("INSERT INTO known_face(image,username) VALUES(?,?)", (self.photo, username))
                    conn.commit()

                    # destroy the window
                    self.root.destroy()

                    # calling another file to operate
                    os.system(' python login.py')
                    break





root=Tk()
obj=Login(root)
# obj.inital(root)
root.mainloop()
