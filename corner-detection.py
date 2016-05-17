#!/usr/bin/env python 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt


img = cv2.imread('figure.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)

corners = np.int0(corners)

X=[]
Y=[]
for corner in corners:

	x,y = corner.ravel()


	cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('img',img)

cv2.waitKey(0)