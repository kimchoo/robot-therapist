from cv2 import *
import numpy as np

cam = cv2.VideoCapture(0)

def snap():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

    ret, frame = cam.read() 
    
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        cam.release() #Release the camera
