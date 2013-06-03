#!/usr/bin/env python
import cv
import sys
from operation import *

file_name = 'scissors_noisy.avi'
des_path = './8_scissors_noisy/'

capture = cv.CaptureFromFile(file_name)
print capture
print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)
print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT)
idx = 0

while True:
    frame = cv.QueryFrame(capture)

    if frame:
        cv.SaveImage( des_path + str(idx) + '.png', frame)
        #cv.ShowImage('Dual',frame)
        #cv.WaitKey(100)
        idx = idx + 1
        print idx
    else:
        break

    # Keyboard interrupt for Exit
    c=cv.WaitKey(2)
    if c==27: #Break if user enters 'Esc'.
        break

