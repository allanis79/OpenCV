#!/usr/bin/env python

import cv2
import numpy as np 

img = cv2.imread('figure.png',cv2.IMREAD_COLOR)
retval, threshold = cv2.threshold(img, 255, 0,cv2.THRESH_BINARY)


print img[0,0]
cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)