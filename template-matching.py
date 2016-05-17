#!/usr/bin/env python

import cv2
import numpy as np 


main = cv2.imread('main.jpg')
main_gray = cv2.cvtColor(main, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(main_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.75

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	#print pt
	cv2.rectangle(main, pt, (pt[0]+w,pt[1]+h), (0,255,255), 2)


cv2.imshow('detected',main)

cv2.waitKey(0)

