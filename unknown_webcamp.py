import shutil

import cv2
import os
import numpy as np
# Open the device at the ID 0

cap = cv2.VideoCapture(0)


i=0
while i<1:
    try:
        path = '/home/yubraj/PycharmProjects/semester_project/Face_Recognition/unknown_faces'
        shutil.rmtree(path)
    except:
        pass

    folder = os.mkdir(f'/home/yubraj/PycharmProjects/semester_project/Face_Recognition/unknown_faces')


    return_value, image = cap.read()
    cv2.imwrite(os.path.join(path,'open' + '.jpg'), image)
    i += 1


    #Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

    os.system('python face.py')





# When everything done, release the capture
# del (cap)
cap.release()
# out.release()
# cv2.destroyWindows('preview')
cv2.waitKey(100000)