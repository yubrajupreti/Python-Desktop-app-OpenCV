# import sqlite3
#
# import face_recognition
# import os
# import cv2
# import numpy as np
# from PIL import Image
# from io import StringIO
# from tkinter import messagebox
#
#
# conn = sqlite3.connect('hito_login.db')
# c=conn.cursor()
#
# KNOWN_FACE_DIR="Known_faces"
# UNKNOWN_FACE_DIR="unknown_faces"
# TOLERANCE=0.6
# FRAME_THICKNESS=3
# FONT_THICKNESS=2
# MODEL="hog"
#
#
# print("loading known faces")
#
# known_faces=[]
# known_name=[]
#
# c.execute("SELECT image,username FROM known_face")
# data=c.fetchall()
#
# def writefile():
#     import pdb;pdb.set_trace()
#     for photo in data:
#         with open(f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Known_faces/{photo[1]}.jpg', 'wb') as file:
#             file.write(photo[0])
#
#
# writefile()
#

#
# for name in os.listdir(KNOWN_FACE_DIR):
#
#     for filename in os.listdir(f"{KNOWN_FACE_DIR}/{name}"):
#         # import pdb;pdb.set_trace()
#         image=face_recognition.load_image_file(f"{KNOWN_FACE_DIR}/{name}/{filename}")
#         print(type(filename))
#         encoding=face_recognition.face_encodings(image)
#         known_faces.append(encoding)
#         known_name.append(name)
#
#
# print("processing unknown faces")
#
# for filename in os.listdir(UNKNOWN_FACE_DIR):
#
#     print(filename)
#     image=face_recognition.load_image_file(f"{UNKNOWN_FACE_DIR}/{filename}")
#     location=face_recognition.face_locations(image, model=MODEL)
#     encoding=face_recognition.face_encodings(image,location)
#     image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
#
#     count=0
#     for face_encoding,face_location in zip(encoding,location):
#         for faces in known_faces:
#
#             results=face_recognition.compare_faces(faces,face_encoding,TOLERANCE)
#             match=None
#             if True in results:
#                 # import pdb;pdb.set_trace()
#                 match=known_name[count]
#                 print(f"match found: {match}")
#                 messagebox.showinfo("Congrats","You are loged in ")
#
#             count=count+1


import os
from tkinter import *


class RegistrationPage:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('500x200')
        master.configure(background="light pink")

        self.fname=StringVar()
        self.lname = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        self.label = Label(master, text="User Registration.",bg="light pink").grid(row=1, column=0, ipadx="10")
        self.label = Label(master, text=" Name", bg="light pink").grid(row=2, column=0, ipadx="10")
        self.label = Label(master, text="Email Id", bg="light pink").grid(row=4, column=0, ipadx="10")
        self.label = Label(master, text="Contact Number", bg="light pink").grid(row=5, column=0, ipadx="10")
        self.label = Label(master, text="DOB", bg="light pink").grid(row=6, column=0, ipadx="10")
        self.label = Label(master, text="Password", bg="light pink").grid(row=7, column=0, ipadx="10")
        self.label = Label(master, text="", bg="light pink").grid(row=8, column=0)

        name = Entry(master,textvariable=self.fname).grid(row=2, column=1)
        self.email = Entry(master).grid(row=4, column=1)
        self.contact = Entry(master).grid(row=5, column=1)
        self.dob = Entry(master).grid(row=6, column=1)
        self.password = Entry(master).grid(row=7, column=1)
        self.submit_button = Button(master, text="Submit", bg="light green", command=self.submit_data).grid(row=8, column=0)
        self.close_button = Button(master, text="Close",  bg="light blue",command=master.quit).grid(row=8, column=2)

    def submit_data(self):
        print("Into submit!")
        name=self.fname.get()
        print(name)

root = Tk()
my_gui = RegistrationPage(root)
root.mainloop()