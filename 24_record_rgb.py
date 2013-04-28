import cv, sys
import cv2
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy as np
from scipy.misc import imresize

fps = 25.0      # so we need to hardcode the FPS
print "Recording at: ", fps, " fps"

frame_size = (640,480)
print "Video size: ", frame_size

rgb_writer = cv.CreateVideoWriter("poll_rgb.avi", cv.CV_FOURCC('X','V','I','D'), fps, frame_size, True)
d_writer = cv.CreateVideoWriter("poll_depth.avi", cv.CV_FOURCC('X','V','I','D'), fps, frame_size, True)

global depth, rgb
while True :

    (depth,_), (rgb,_) = get_depth(), get_video()

    # Depth
    d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
    binary_img = cv.fromarray(np.array(d3[:,:,::-1]))

    cv.SaveImage('shit.png', binary_img) #Saves the image
    shit=cv.LoadImage('shit.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
    image = cv.CreateImage ((640,480), 8, 3)
    bitmap = cv.CreateImageHeader((640, 480), cv.IPL_DEPTH_8U, 3)
    cv.SetData(bitmap, shit.tostring())

    cv.WriteFrame(d_writer, image)

    cv.ShowImage("depth",image)

    # RGB
    binary_img = cv.fromarray(np.array(rgb[:,:,::-1]))
    cv.SaveImage('shit.png', binary_img) #Saves the image
    shit=cv.LoadImage('shit.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
    image = cv.CreateImage ((640,480), 8, 3)
    bitmap = cv.CreateImageHeader((640, 480), cv.IPL_DEPTH_8U, 3)
    cv.SetData(bitmap, shit.tostring())

    cv.WriteFrame(rgb_writer, image)


    cv.ShowImage("rgb",image)
    cv.WaitKey(2)
