import numpy as np
import cv2

def cam_snap():

    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

    rnt, image = cam.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage)
 
    cv2.waitKey(0)
    cam.release()

    return faces, grayImage
