import shutil
import sqlite3

import face_recognition
import os
import cv2

from tkinter import messagebox

# connection made with database
conn = sqlite3.connect('hito_login.db')
c=conn.cursor()

# fetching the image and username of regiseter user for authentication
c.execute("SELECT image,username FROM known_face")
data=c.fetchall()

# method define to convert blob image into normal form for encoding
def importPhoto():
    # make folder known_face in the system
    folder = os.mkdir(f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Known_faces')

    # write the fetch image in folder known_face with username as name of image file
    for photo in data:
        with open(f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Known_faces/{photo[1]}.jpg', 'wb') as file:
            file.write(photo[0])

    # calling another method
    face()




def face():

    known_faces=[]
    known_name=[]

    # name of the folder where regiseter face are fetched and stored
    KNOWN_FACE_DIR="Known_faces"

    # name of the folder where current user image is store for validation
    UNKNOWN_FACE_DIR="unknown_faces"

    # define the accuracy match of images
    TOLERANCE = 0.6
    MODEL = "hog"

    # loop in known_face directory
    for name in os.listdir(KNOWN_FACE_DIR):

        # load the image and convert  <class 'str'> into <class numpy.array> for encoding
        image=face_recognition.load_image_file(f"{KNOWN_FACE_DIR}/{name}")

        # image file is encoded for comparing
        encoding=face_recognition.face_encodings(image)

        # encoded data appended in list
        known_faces.append(encoding)
        known_name.append(name)


    print("processing unknown faces")

    # loop in unknown folder where user current image is loaded.
    for filename in os.listdir(UNKNOWN_FACE_DIR):

        image=face_recognition.load_image_file(f"{UNKNOWN_FACE_DIR}/{filename}")
        location=face_recognition.face_locations(image, model=MODEL)
        encoding=face_recognition.face_encodings(image,location)
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        count=0
        found = False
        # comaparing the regiseter iamge with unknown image
        for face_encoding,face_location in zip(encoding,location):
            for faces in known_faces:

                results=face_recognition.compare_faces(faces,face_encoding,TOLERANCE)
                match=None

                # condition to run when match is true i.e the value of result should be true
                if True in results:
                    found=True
                    match=known_name[count]
                    print(f"match found: {match}")

                    os.system('python home.py')

        if found==False:
            messagebox.showerror("Error", "Not Register Identity ")



    known_folder = '/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Known_faces'
    unknown_folder='/home/yubraj/PycharmProjects/semester_project/Face_Recognition/unknown_faces'

    # shutil function is used to delete the folder after the operation is over
    shutil.rmtree(known_folder)
    shutil.rmtree(unknown_folder)


# function calling
importPhoto()























    #             top_left=(face_location[3],face_location[0])
    #             bottom_right=(face_location[1],face_location[2])
    #             color=[0,255,0]
    #             cv2.rectangle(image, top_left,bottom_right,color,FRAME_THICKNESS)
    #
    #             top_left = (face_location[3], face_location[2])
    #             bottom_right = (face_location[1], face_location[2]+22)
    #             cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
    #             cv2.putText(image, match, (face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
    #         count = count + 1
    # # import pdb;pdb.set_trace()
    # cv2.imshow(filename,image)
    # cv2.waitKey(10000)


