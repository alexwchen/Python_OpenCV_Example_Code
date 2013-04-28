from freenect import sync_get_depth as get_depth, sync_get_video as get_video
from scipy.misc import imresize
from operation import *
import numpy as np
import cv, sys
import cv2

fps = 25.0      # so we need to hardcode the FPS
print "Recording at: ", fps, " fps"

frame_size = (640,480)
print "Video size: ", frame_size

writer = cv.CreateVideoWriter("original.avi", cv.CV_FOURCC('X','V','I','D'), fps, frame_size, True)

global depth, ir
while True :

    (depth,_), (ir,_) = get_depth(), get_video(format=2)

    # Process Depth Matrix to Binary Matrix
    binary = (ir>200).astype(float)
    binary = binary*255

    im = imresize(binary, (480,640))
    binary_img = cv.fromarray(im)

    cv.ShowImage("original",binary_img)

    cvMat = cvMat_to_iplimage_grayscale(binary_img)
    image = cv.CreateImage (frame_size, 8, 3)
    bitmap = cv.CreateImageHeader(frame_size, cv.IPL_DEPTH_8U, 3)
    cv.SetData(bitmap, cvMat.tostring())
    cv.WriteFrame(writer, image)

    cv.WaitKey(2)
