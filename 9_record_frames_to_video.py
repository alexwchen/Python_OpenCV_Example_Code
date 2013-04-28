import cv, sys
import cv2
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy as np
from scipy.misc import imresize

fps = 25.0      # so we need to hardcode the FPS
print "Recording at: ", fps, " fps"

frame_size = (640,480)
print "Video size: ", frame_size

writer = cv.CreateVideoWriter("scissor_noisy.avi", cv.CV_FOURCC('X','V','I','D'), fps, frame_size, True)

global depth, rgb
while True :

    (depth,_), (rgb,_) = get_depth(), get_video()

    # Process Depth Matrix to Binary Matrix
    binary = (depth==2047).astype(int)
    binary = binary[:, :-10]

    # 400 is width, 300 is height
    binary_resize = imresize(binary, (480,640))
    binary_img = cv.fromarray(binary_resize)

    cv.SaveImage('shit.png', binary_img) #Saves the image
    shit=cv.LoadImage('shit.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image

    image = cv.CreateImage ((640,480), 8, 3)

    bitmap = cv.CreateImageHeader((640, 480), cv.IPL_DEPTH_8U, 3)
    cv.SetData(bitmap, shit.tostring())

    cv.WriteFrame(writer, image)

    cv.ShowImage("show_img",image)
    cv.WaitKey(2)
