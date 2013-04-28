from freenect import sync_get_depth as get_depth, sync_get_video as get_video
from scipy.misc import imresize
import numpy as np
import cv, sys
import cv2

capture=cv.CaptureFromCAM(0)
fourcc = cv.CV_FOURCC('X','V','I','D')
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FPS, 30)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

global depth, ir
while True :

    (depth,_), (ir,_) = get_depth(), get_video(format=2)
    """
    rgb = cv.QueryFrame(capture)
    cv.ShowImage('RGB',rgb)
    """
    # Build a two panel color image
    d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
    ir3 = np.dstack((ir, ir, ir)).astype(np.uint8)

    depth_ir = np.hstack((d3,ir3))

    # Form Frame/Image
    image = cv.fromarray(np.array(depth_ir[:,:,::-1]))


    # Playback Frame
    cv.ShowImage('Dual',image)
    cv.WaitKey(5)

    # Keyboard interrupt for Exit
    c=cv.WaitKey(2)
    if c==27: #Break if user enters 'Esc'.
        break


    cv.WaitKey(2)
