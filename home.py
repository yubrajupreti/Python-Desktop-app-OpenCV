# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:43:45 2020

@author: Koki
"""

import os
from tkinter import *
from PIL import Image, ImageTk
#from voiceAssistantEdit import myQuery

# from login import active_user
#
# print(active_user)

#
# def user():
#     return active_user
#

def loadTest():
    root.destroy()
    os.system('python cubetest.py')

# creating tkinter window
root = Tk()
root.title("HITO")
root.geometry("1360x680+0+0")
root.minsize(1280, 690)

title = Label(root, text="Welcome", font=("times new roman", 30, "bold"), bg="green", fg="yellow", bd=10, relief=GROOVE)
title.place(x=0, y=0, relwidth=1)

#putting image
face = Image.open("Photo/user_photo.png")
resize_face = face.resize((300, 300), Image.ANTIALIAS)
face_icon = ImageTk.PhotoImage(resize_face)


panel = Label(root, image = face_icon, bg = 'white', bd = 10)
panel.place(relx = .43, rely = .25)

cube_button = Button(root,text="Cube Test", pady = 5, command = loadTest, width=15,font=("times new roman",14,"bold"),bg="Green",fg="black").place(relx = 0.5, rely = 0.85, anchor = CENTER)

# Creating a photoimage object to use image
#photo = PhotoImage(file = r"C:\Users\HP\python\Advanced Programming assignment\voice.png")

# Resizing image to fit on button
#photoimage = photo.subsample(16, 16)

# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
#voice_button = Button(root, text = 'Voice Recognition', pady = 5, command = myQuery, image = photoimage,font=("times new roman",14,"bold"),padx=5,bg="Green",fg="black", compound = LEFT, activebackground = "Red").place(relx = 0.3, rely = .85, anchor = CENTER)
root.mainloop()

