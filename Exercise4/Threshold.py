# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:09:48 2017

@author: zhangzhexi
"""

import cv2

def main():
    image = cv2.imread("Test_images/Lenna.png",1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Input Image',gray)
    cv2.imwrite('Input_image.jpg',gray)
    
    threshold_value = 128
    dst,thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)
    cv2.imshow("Threshold Image", thresh)
    cv2.imwrite("Threshold_image.jpg",thresh)

#    Binary Threshold
    dst,thresh_binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary threshold", thresh_binary)
    cv2.imwrite("Threshold_binary.jpg", thresh_binary)

#    Band Thresholding
    threshold1 = 27
    threshold2 = 125
    dst,binary_image_1 = cv2.threshold(gray, threshold1, 255, cv2.THRESH_BINARY)
    dst,binary_image_2 = cv2.threshold(gray, threshold2, 255, cv2.THRESH_BINARY_INV)
    band_thresholded_image = cv2.bitwise_and(binary_image_1,binary_image_2)
    cv2.imshow("Band Thresholding", band_thresholded_image)
    cv2.imwrite("Band_Thresholding.jpg", band_thresholded_image)

#   Semi Thresholding
    current_threshold = 128
    max_threshold = 255;
    dst,semi_thresholded_image = cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    semi_thresholded_image = cv2.bitwise_and(gray,semi_thresholded_image)
    cv2.imshow("Semi Thresholding",semi_thresholded_image)
    cv2.imwrite("Semi_Thresholding.jpg",semi_thresholded_image)

#   Adaptive Thresholding
    adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
    cv2.imshow("Adaptive Thresholding", adaptive_thresh)
    cv2.imwrite("Adaptive_Thresholding.jpg", adaptive_thresh)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
