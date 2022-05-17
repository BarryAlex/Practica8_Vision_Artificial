#Edwing Alexis Casillas Valencia.   19110113.   7E1.    Práctica 8 visión artificial
#Deteccion de bordes: Laplaciano, Sobelx, Sobely, Canny
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,100,200)


    cv2.imshow('Original',frame)
    cv2.imshow('Laplaciano',laplacian)
    cv2.imshow('SobelX',sobelx)
    cv2.imshow('SobelY',sobely)
    cv2.imshow('Edges',edges)

    if cv2.waitKey(1) & 0xFF == ord('0'):
        break

cv2.destroyAllWindows()
cap.release()
