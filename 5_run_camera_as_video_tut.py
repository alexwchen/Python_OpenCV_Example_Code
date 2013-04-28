import cv
capture=cv.CaptureFromCAM(0)

fourcc = cv.CV_FOURCC('X','V','I','D')
fps = 25.0 # or 30.0 for a better quality stream
#writer = cv.CreateVideoWriter("output.avi", fourcc, 25.0, (640,480), is_color=1)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FPS, 30)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
    image=cv.QueryFrame(capture)
    cv.ShowImage('Dual',image)

    #cv.WriteFrame(writer, image)
    cv.WaitKey(2)


