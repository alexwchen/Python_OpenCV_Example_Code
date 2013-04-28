import cv
import cv2
import numpy as np
from scipy.misc import imresize
# Since I don't know how to exchange between iplimage & cvMat
# Now, here is the plan
# Load as cvMat
# cv_Mat -> ndarray using asarray np.asarray()
# Do all computation with ndaaray
# Change it back to iplimage using cv.fromarray
# Diplay it



# Load Image as matrix (cv.LoadImageM)
mat = cv.LoadImageM('picture.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
print "Now is cvMat format"
print "Type, Height, Width: ", type(mat), mat.width, mat.height


# Convert to ndarray
narray = np.asarray(mat)
print "Now is ndarray format"
print "Numpy Ndarray: ", narray.shape
#print "MAX VALUE", max(narray)
#print "MIN VALUE", min(narray)

# Convert to iplimage
image = cv.fromarray(narray)



# Complicated version, please reference rectangle_kinect.py
#image = cv.fromarray(np.array(da[:,:,::-1]))
source = cv2.imread('picture.png') # source is numpy array
bitmap = cv.CreateImageHeader((source.shape[1], source.shape[0]), cv.IPL_DEPTH_8U, 3)
cv.SetData(bitmap, source.tostring(),
                   source.dtype.itemsize * 3 * source.shape[1])



# Playback Frame
cv.ShowImage('display',bitmap)

cv.WaitKey(10000)


# Here is how to load numpy array directly
