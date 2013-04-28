#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv
import cv2
import numpy as np

def doloop():
    global depth,ir, rgb

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

        (depth,_), (ir,_) = get_depth(), get_video(format=2)


        # How does Downsample Works
        # ::2, means you skip by 2 -> [1,2,3,4] -> [2,4]
        # Downsample col -> cv.fromarray(np.array(rgb[:, ::2, ::-1]))
        # Downsample row -> cv.fromarray(np.array(rgb[::2, :, ::-1]))
        # Color Chanel: All Color -> cv.fromarray(np.array(rgb[::2, ::2, ::-1]))
        # Color Chanel: Blue      -> cv.fromarray(np.array(rgb[::2, ::2]))
        # Color Chanel: Gray      -> cv.fromarray(np.array(rgb[::2, ::2, 0]))

        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        i3 = np.dstack((ir, ir, ir)).astype(np.uint8)
        da = np.hstack((d3,i3))

        # Form Frame/Image
        image = cv.fromarray(np.array(da[:,:,::-1]))

        # Playback Frame
        cv.ShowImage('Dual',image)
        cv.WaitKey(5)

        # Keyboard interrupt for Exit
        c=cv.WaitKey(2)
        if c==27: #Break if user enters 'Esc'.
            break
doloop()
