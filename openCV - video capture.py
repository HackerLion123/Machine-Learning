
# coding: utf-8

# In[8]:


import cv2
import urllib
import numpy as np
import requests
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
	ret,frame = cap.read()
    
	if ret == True:
		gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
		#set threshold to the image 127 - lowerbound 255-upper bound it converts image to either white 1 or black 0
		#ret,thresh1 = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)      #global thresholding
		#gray_img = thresh1

		gray_img = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #plt.imshow(gray_img)
        #plt.show()
		_,contor,_ = cv2.findContours(gray_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		print("no of shapes {0}".format(len(contor)))

		for cnt in contor:
			epsilon = 0.1*cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,epsilon,True)
			cnt = approx
			rect = cv2.minAreaRect(cnt)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			cv2.drawContours(frame,[box],0,(0,255,0),3)

		cv2.imshow('frame',frame);
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break;
	else:
		break;

#check if optimization is enabled
cv2.useOptimized()

