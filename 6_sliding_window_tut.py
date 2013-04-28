import cv
from math import ceil

# Original Image
image=cv.LoadImage('picture.png', cv.CV_LOAD_IMAGE_GRAYSCALE) #Load the image

# Get Image Size
MAX_X,MAX_Y=cv.GetSize(image)
print MAX_X
print MAX_Y

# Sliding Window Size
pos_x = 0
pos_y = 0
wx = 50
wy = 50
pixel_jump = 10

# Window Multiplier
MULT = 10

for mult in range(MULT):
    wx = int(wx*(mult*0.1+1))
    wy = int(wy*(mult*0.1+1))

    # slide through vertical
    while(pos_y + wy < MAX_Y):

        # slide through horizontal
        while(pos_x + wx < MAX_X):

            # draw rectangle and show image
            clone_img = cv.CloneImage(image)
            cv.Rectangle(clone_img, (pos_x,pos_y), (pos_x+wx,pos_y+wy), (255,255,255), 1,0)
            cv.ShowImage("clone",clone_img)
            cv.WaitKey(10)

            # increment
            pos_x = pos_x + pixel_jump

       # increment
        pos_x = 0
        pos_y = pos_y + pixel_jump

    # reset position
    pos_x = 0
    pos_y = 0

"""
cv.Rectangle(image, (100,100), (540,540), (0,255,0))

# Get Template
cv.SetImageROI(image, (100,100,50,50))
template=cv.CloneImage(image)

cv.ResetImageROI(image)
cv.ShowImage("image",image)
cv.WaitKey(10000)

cv.ShowImage("template",template)
cv.WaitKey(10000)
"""
