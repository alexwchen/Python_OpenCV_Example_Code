#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
from operation import *
import numpy as np
import cv
import cv2


def doloop():

    capture=cv.CaptureFromCAM(0)
    fourcc = cv.CV_FOURCC('X','V','I','D')
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FPS, 30)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    global depth,ir, rgb
    count = 0

    while True:
        rgb_frame=cv.QueryFrame(capture)
        rgb = iplimage_to_numpy_color(rgb_frame)

        (depth,_), (ir,_) = get_depth(), get_video(format=2)
        np.resize(depth, (300,400))
        np.resize(ir, (300,400))
        np.resize(rgb, (300,400,3))

        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        ir3 = np.dstack((ir, ir, ir)).astype(np.uint8)
        depth_ir = np.hstack((d3,ir3))

        # Form Frame/Image
        image = cv.fromarray(np.array(depth_ir[:,:,::-1]))
        rgb_image = numpy_to_iplimage_color(rgb)

        d_cvMat = cv.fromarray(np.array(d3[:,:,::-1]))
        depth_image = cvMat_to_iplimage_color(d_cvMat)


        opacity = 0.4
        cv.AddWeighted(depth_image, opacity, rgb_image, 1 - opacity, 0, rgb_image)

        # Playback Frame
        cv.ShowImage('Trio',image)
        cv.ShowImage('RGB',rgb_image)
        cv.WaitKey(5)

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break


        # How does Downsample Works
        # ::2, means you skip by 2 -> [1,2,3,4] -> [2,4]
        # Downsample col -> cv.fromarray(np.array(rgb[:, ::2, ::-1]))
        # Downsample row -> cv.fromarray(np.array(rgb[::2, :, ::-1]))
        # Color Chanel: All Color -> cv.fromarray(np.array(rgb[::2, ::2, ::-1]))
        # Color Chanel: Blue      -> cv.fromarray(np.array(rgb[::2, ::2]))
        # Color Chanel: Gray      -> cv.fromarray(np.array(rgb[::2, ::2, 0]))
        """
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        i3 = np.dstack((ir, ir, ir)).astype(np.uint8)
        da = np.hstack((d3,i3))

        # Form Frame/Image
        image = cv.fromarray(np.array(da[:,:,::-1]))
        cv.Rectangle(image, (50,10), (590,450), (0,255,0))

        # Playback Frame
        cv.ShowImage('Dual',image)
        cv.WaitKey(5)

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break
        """
doloop()
