#!/usr/bin/env python

import cv2
import numpy as np 


img = cv2.imread('figure.png',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(250,250),(255,0,0),15)

cv2.rectangle(img,(15,25),(200,150),(0,255,0),15)
cv2.circle(img,(100,63),55,(0,0,255),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destoryAllWindows()