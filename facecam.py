from cv2 import *
import numpy as np

#Psuedo Code:
#   because the open cv read() method is only called once (outside a loop). the program will only work with a single picture (hence the snap name)
#   firstly the image is converted to grey scale to reduce the neccesary compation
#   then the face_casacde obj is used to produce a face detector, based of the xml file.
#   after all is done release the camera and rtn the faces seen

cam = cv2.VideoCapture(0) #Define a video camera to use.

def snap():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml') #Create a face detection obj

    ret, frame = cam.read() #Read the image from the "cam" obj
        
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert the image to grey-scale

        faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Apply the face detection to the grey-scale image
        
        cam.release() #Release the camera
