#!/usr/bin/env python

import cv2
import numpy as np

cap = cv2.VideoCapture('SAP.avi')
fgbg = cv2.BackgroundSubtractorMOG2()

while cap.isOpened():
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	
	cv2.imshow('original',frame)
	
	cv2.imshow('fg',fgmask)
	

	k = cv2.waitKey(30) & 0xff

	if k == 27:
		break
	

cap.release()
cv2.destroyAllWindows()
