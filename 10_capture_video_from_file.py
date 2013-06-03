#!/usr/bin/env python

import cv
import sys

files = sys.argv[1:]

print files

for f in files:
    capture = cv.CaptureFromFile(f)
    print capture
    print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)
    print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT)

    while True:
        frame = cv.QueryFrame(capture)

        if frame:
            print frame
            print type(frame)
            cv.ShowImage('Dual',frame)
            cv.WaitKey(100)

        else:
            break

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break

