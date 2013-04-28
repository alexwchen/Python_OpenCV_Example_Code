#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
from scipy.misc import imresize
from operation import *
import cv
import cv2
import numpy as np


def doloop():

    capture=cv.CaptureFromCAM(0)
    fourcc = cv.CV_FOURCC('X','V','I','D')
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FPS, 30)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    global depth,ir, rgb
    count = 0

    while True:

        # Web cam
        rgb_ipl =cv.QueryFrame(capture)
        rgb_np = iplimage_to_numpy_color(rgb_ipl)

        # Kinect cam
        (ir,_) = get_video(format=2)
        ir3 = np.dstack((ir, ir, ir)).astype(np.uint8)
        ir_cvMat = cv.fromarray(ir)
        ir_ipl = cvMat_to_iplimage_color(ir_cvMat)

        # Resize and Crop x,y,w,h
        cv.SetImageROI(ir_ipl, (95,0,500,380))
        ir_np = iplimage_to_numpy_color(ir_ipl)

        ir_np = imresize(ir_np, (480, 640))
        #print ir_np.shape
        ir_cvMat = cv.fromarray(ir_np)
        ir_ipl = cvMat_to_iplimage_color(ir_cvMat)

        cv.ShowImage('ir',ir_ipl)
        cv.ShowImage('rgb',rgb_ipl)

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break

doloop()
