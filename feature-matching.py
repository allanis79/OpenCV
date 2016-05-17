#!/usr/bin/env python 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

main = cv2.imread('objects.jpg')
template = cv2.imread('pillow.jpg')


orb = cv2.ORB()


kp1,des1 = orb.detectAndCompute(main,None)
kp2,des2 = orb.detectAndCompute(template,None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2 )

matches = sorted(matches, key = lambda x:x.distance)



img3  = cv2.drawMatches(main,kp1,template,kp2,matches[:30],None,flags =2)


plt.imshow(img3)
plt.show()