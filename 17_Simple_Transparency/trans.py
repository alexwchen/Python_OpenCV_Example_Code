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


# (3) blend with the original:
opacity = 0.4

cv.AddWeighted(overlay, opacity, original, 1 - opacity, 0, original)
cv.ShowImage('Real Time Recognition', original)
cv.WaitKey(10000)
