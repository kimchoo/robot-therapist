from cv2 import *

#Psuedo Code:
#   because the open cv read() method is only called once (outside a loop). the program will only work with a single picture (hence the snap name)
#   firstly the image is converted to grey scale to reduce the neccesary compation
#   then the face_casacde obj is used to produce a face detector, based of the xml file.
#   after all is done release the camera and rtn the faces seen

cam = cv2.VideoCapture(0)

def snap():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
           
    cam.release()

    return faces
