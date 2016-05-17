#!/usr/bin/env python

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('figure.png')#,cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img,cmap = 'gray',interpolation='bicubic')
plt.plot([50,150],[30,70],'c',linewidth = 7)
plt.show()