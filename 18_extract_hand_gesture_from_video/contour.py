import numpy as np
import cv
import cv2
import os
from scipy.misc import imresize


def crop_largest_contour(im):

    # Process Contour
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(im,contours,-1,(0,255,0),3)


    # Loop through all possible contour find max
    max_area = 0
    param = [0,0,0,0]
    for i in contours:
        x,y,w,h = cv2.boundingRect(i)

        if w*h>max_area:
            max_area = w*h
            param = [x,y,w,h]

    x = param[0]
    y = param[1]
    w = param[2]
    h = param[3]

    #cv2.rectangle(im,(x,y),(x+w, y+h),(0,255,255),2)


    # Numpy->Iplimage
    source = im # source is numpy array
    image = cv.CreateImageHeader((source.shape[1], source.shape[0]), cv.IPL_DEPTH_8U, 3)
    cv.SetData(image, source.tostring(),
                       source.dtype.itemsize * 3 * source.shape[1])
    cv.SetImageROI(image, (x,y,x+w,y+h))
    cv.SaveImage('hack.png', image) #Saves the image

    # Hack 2 - Resize
    image=cv.LoadImageM('hack.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
    resize_image = imresize(image, (40,40))
    source = resize_image
    image = cv.CreateImageHeader((source.shape[1], source.shape[0]), cv.IPL_DEPTH_8U, 3)
    cv.SetData(image, source.tostring(),
                       source.dtype.itemsize * 3 * source.shape[1])

    return image

def process_all_files():

    for r,d,file_list in os.walk('./'):

        count=0
        for f in file_list:
            print f
            if str(f)[-4:]=='.png':
                im = cv2.imread(str(f))[:, :-10]
                image = crop_largest_contour(im)
                c = cv.WaitKey(10)
                if c==27:
                    break

                # Save Image in previous directory
                cv.SaveImage('../'+str(count)+'.png', image) #Saves the image
                count = count + 1
        # Get rid of all temporary files
        os.system('rm hack.png')

process_all_files()

