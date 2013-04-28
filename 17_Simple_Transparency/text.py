#!/usr/bin/env python
import cv2
import cv
from operation import *

original = cv.LoadImage('lena-eyes.png', cv.CV_LOAD_IMAGE_COLOR)

# (1) create a copy of the original:
overlay = cv.CloneImage(original)


# (2) draw shapes:
cv.Circle(original, (13, 132), 12, (0, 255, 0), -1)
cv.Circle(original, (16, 132), 12, (0, 255, 0), -1)

# (3) create fonts
#Font Options
#CV_FONT_HERSHEY_SIMPLEX 0
#CV_FONT_HERSHEY_PLAIN 1
#CV_FONT_HERSHEY_DUPLEX 2
#CV_FONT_HERSHEY_COMPLEX 3
#CV_FONT_HERSHEY_TRIPLEX 4
#CV_FONT_HERSHEY_COMPLEX_SMALL 5
#CV_FONT_HERSHEY_SCRIPT_SIMPLEX 6
#CV_FONT_HERSHEY_SCRIPT_COMPLEX 7
#InitFont(fontFace, hscale, vscale, shear=0, thickness=1, lineType=8)

font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 0.5, 0.5, 0, 1, 5) #Creates a font
x = 100
y = 100
cv.PutText(original,"Hello World!!!", (x,y),font, (255,255,255)) #Draw the text

# (4) blend with the original:
opacity = 0.4
cv.AddWeighted(overlay, opacity, original, 1 - opacity, 0, original)



cv.ShowImage('Real Time Recognition', original)
cv.WaitKey(10000)
