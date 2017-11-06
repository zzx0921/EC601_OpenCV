# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

lena = cv2.imread('Test_images/Lenna.png') #load Lenna image

[b,g,r] = cv2.split(lena) #split into color channels

cv2.imshow('Blue',b)
cv2.imwrite('Blue.png',b)
cv2.imshow('Red',r) 
cv2.imwrite('Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('Green.png',g)

print(lena[20,25])

hsv_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV) #convert to HSV

[h,s,v] = cv2.split(hsv_lena) #split into HSV channels

cv2.imshow('Hue',h)
cv2.imwrite('Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('Value.png',v)

print(hsv_lena[20,25])

YCC_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb

[y,Cb,Cr] = cv2.split(YCC_lena) #split YCrCb channels

cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)

print(YCC_lena[20,25])

cv2.waitKey(0)
