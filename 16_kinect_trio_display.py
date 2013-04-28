#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv
import cv2
import numpy as np

def doloop():
    global depth,ir, rgb
    count = 0

    (depth,_), (rgb,_) = get_depth(), get_video(format=0)
    (depth,_), (ir,_) = get_depth(), get_video(format=2)
    np.resize(depth, (300,400))
    np.resize(ir, (300,400))
    np.resize(rgb, (300,400,3))

    while True:
        """
        ctypedef enum freenect_video_format:
        FREENECT_VIDEO_RGB
        FREENECT_VIDEO_BAYER
        FREENECT_VIDEO_IR_8BIT
        FREENECT_VIDEO_IR_10BIT
        FREENECT_VIDEO_IR_10BIT_PACKED
        FREENECT_VIDEO_YUV_RGB
        FREENECT_VIDEO_YUV_RAW
        """

        # frame rate control
        count = count + 1
        if count == 5:
            count = 0
            idx = 1
        else:
            idx = 0

        # update frame
        if idx:
            foridx = idx*2
            (depth,_), (ir,_) = get_depth(), get_video(format=foridx)
            np.resize(depth, (300,400))
            np.resize(ir, (300,400))
        else:
            foridx = idx*2
            (depth,_), (rgb,_) = get_depth(), get_video(format=foridx)
            np.resize(depth, (300,400))
            np.resize(rgb, (300,400,3))

        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        ir3 = np.dstack((ir, ir, ir)).astype(np.uint8)

        depth_ir = np.hstack((d3,ir3))
        dep_ir_rgb = np.hstack((depth_ir,rgb))

        # Form Frame/Image
        image = cv.fromarray(np.array(dep_ir_rgb[:,:,::-1]))

        # Playback Frame
        cv.ShowImage('Trio',image)
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
