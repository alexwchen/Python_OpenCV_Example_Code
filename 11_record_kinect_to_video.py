#!/usr/bin/env python
import cv, sys
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy as np
from scipy.misc import imresize

fps = 25.0      # so we need to hardcode the FPS
print "Recording at: ", fps, " fps"

frame_size = (300, 400)
print "Video size: ", frame_size

writer = cv.CreateVideoWriter("out.avi", cv.CV_FOURCC('X','V','I','D'), fps, frame_size, True)

def doloop():
    global depth, rgb
    count = 0

    while True:

        # Get a fresh frame
        (depth,_), (rgb,_) = get_depth(), get_video()

        # Process Depth Matrix to Binary Matrix
        binary = (depth==2047).astype(int)

        # 400 is width, 300 is height
        binary_resize = imresize(binary, (300,400))
        binary_img = cv.fromarray(binary_resize)

        cv.SaveImage('tmp.png', binary_img) #Saves the image
        shit=cv.LoadImage('tmp.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
        cv.SaveImage('tmp.png', shit) #Saves the image

        cv.WriteFrame(writer, shit)

        # Playback Frame
        cv.NamedWindow('Binary', cv.CV_WINDOW_AUTOSIZE)
        cv.ShowImage('Binary', binary_img)
        cv.WaitKey(5)

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break
    #cv.ReleaseVideoWriter(writer)
doloop()

