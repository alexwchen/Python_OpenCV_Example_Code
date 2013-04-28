import numpy as np
import cv
import cv2

# Load Image
im = cv2.imread('1017.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
print type(im)
# Process Contour
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

cv2.rectangle(im,(x,y),(x+w, y+h),(0,255,255),2)


# Numpy->Iplimage
source = im # source is numpy array
image = cv.CreateImageHeader((source.shape[1], source.shape[0]), cv.IPL_DEPTH_8U, 3)
cv.SetData(image, source.tostring(),
                   source.dtype.itemsize * 3 * source.shape[1])
cv.SetImageROI(image, (x,y,w,h))

# Display Image
cv.SaveImage('hack.png', image) #Saves the image
image=cv.LoadImage('hack.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
cv.SetImageROI(image, (0,0,w,h))


cv.ShowImage('window', image) #Show the image

# CV wait key 0 means halt
cv.WaitKey(0)
