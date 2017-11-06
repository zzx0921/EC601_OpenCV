#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:42:28 2017

@author: zhangzhexi
"""
import cv2
import numpy as np
import random

def Add_salt_pepper_Noise(image,pa,pb):
    row,col,ch=image.shape
    amount1=row*col*pa
    amount2=row*col*pb
    for i in range(int(amount1)):
        image[int(random.uniform(0,row))][int(random.uniform(0,col))]=0
    for i in range(int(amount2)):
        image[int(random.uniform(0,row))][int(random.uniform(0,col))]=255

def Add_gaussian_Noise(src,mean,sigma):
    noiseArr = src.copy()
    noiseArr = np.random.normal(mean,sigma,src.shape)
    np.add(src,noiseArr,src,casting="unsafe")
    return;

def main():
    img=cv2.imread('Test_images/Lenna.png')
    cv2.namedWindow('Original image')
    cv2.imshow('Original',img)
    cv2.imwrite('Original.jpg',img)
    
    noise_img=img.copy()
    Add_gaussian_Noise(noise_img,0,50)
    cv2.imshow('Gaussian Noise',noise_img)
    cv2.imwrite('Gaussian_Noise.jpg',noise_img)
    
    noise_dst=noise_img.copy()
    cv2.blur(noise_dst,(3,3))
    cv2.imshow('Box filter',noise_dst)
    cv2.imwrite('Box_filter.jpg',noise_dst)
    
    noise_dst1=noise_img.copy()
    cv2.GaussianBlur(noise_dst1,(3,3),1.5)
    cv2.imshow('GaussianBlur filter',noise_dst1)
    cv2.imwrite('Gaussian_Blur_filter.jpg',noise_dst1)
    
    noise_dst2=noise_img.copy()
    cv2.medianBlur(noise_dst2,3)
    cv2.imshow('Median filter',noise_dst2)
    cv2.imwrite('Median_filter.jpg',noise_dst2)
    
    noise_img2=img.copy()
    pa=0.01     #Controls the amount of black spots in the noise
    pb=0.01     #Controls the amount of white spots in the noise
    Add_salt_pepper_Noise(noise_img2,pa,pb)
    cv2.imshow("Salt and Peper Noise", noise_img2)
    cv2.imwrite("Salt_and_Peper_Noise.jpg", noise_img2)
    
    noise_dst3=noise_img2.copy()
    cv2.blur(noise_dst3,(3,3))
    cv2.imshow('Box filter2',noise_dst3)
    cv2.imwrite('Box_filter2.jpg',noise_dst3)
    
    noise_dst4=noise_img2.copy()
    cv2.GaussianBlur(noise_dst4,(3,3),1.5)
    cv2.imshow('Gaussian Blur filter2',noise_dst4)
    cv2.imwrite('Gaussian_Blur_filter2.jpg',noise_dst4)
    
    noise_dst5=noise_img2.copy()
    cv2.medianBlur(noise_dst5,3)
    cv2.imshow('Median filter2',noise_dst5)
    cv2.imwrite('Median_filter2.jpg',noise_dst5)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    
