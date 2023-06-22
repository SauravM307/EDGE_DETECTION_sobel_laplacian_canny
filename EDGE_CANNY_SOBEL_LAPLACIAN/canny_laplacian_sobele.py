#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:17:36 2023

@author: sauravmishra
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
def apply_sobel(img_blur):
    #Aplly sobel edge detection in the x and y directions

    sobelx=cv2.Sobel(img_blur,cv2.CV_64F,1,0,ksize=3)
    sobely=cv2.Sobel(img_blur,cv2.CV_64F,0,1,ksize=3)

    #combining the two gradients top prodcue an edge map

    sobel=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
    sobel_map=sobel*img_blur
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_sobel_map.png',sobel_map)
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_sobel.png',sobel)


def apply_laplacian(img_blur):
    
    laplacian=cv2.Laplacian(img_blur,cv2.CV_64F)
    #Threshold the edge map
    thresh=np.max(laplacian)/20
    laplacian[laplacian<thresh]=0
    laplacian[laplacian>=thresh]=255
    laplacian_map=laplacian*img_blur;
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_laplacian_map.png',laplacian_map)
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_laplacian.png',laplacian)
    
def apply_canny(img_blur):
    canny=cv2.Canny(img_blur,25,230)
    canny_map=canny*img_blur
    
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_canny.png',canny)
    cv2.imwrite('/Users/sauravmishra/Desktop/HDR_canny_map.png',canny_map)    
    
if __name__ == "__main__":
    img=cv2.imread('/Users/sauravmishra/Desktop/HDRimg.hdr');
    img_original = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #img_blur=cv2.GaussianBlur(img,(3,3),0)
    img_blur=img_original

    apply_sobel(img_blur)
    
    
    #applying laplacian edge detection
    apply_laplacian(img_blur)

    apply_canny(img_blur)