import sqlite3

import cv2
import os




def convertToBinaryData(filename):

    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def webcamp():
    a=10
    conn = sqlite3.connect('hito_login.db')
    c=conn.cursor()

    # Open the device at the ID 0
    cap = cv2.VideoCapture(0)


    # folder=os.mkdir(f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Known_faces/{username}')


    i=0

    while i<1:

        path = f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Access_photo'

        return_value, image = cap.read()
        cv2.imwrite(os.path.join(path,'first'+'.jpg'), image)
        i += 1

        photo = convertToBinaryData(
            f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/Access_photo/first.jpg')

        # print(photo)

        i += 1


        #Waits for a user input to quit the application

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    # When everything done, release the capture
    # del (cap)
    cap.release()
    # out.release()
    # cv2.destroyWindows('preview')
    cv2.waitKey(100000)
    return photo

webcamp()


