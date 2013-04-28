import cv
from scipy.misc import imresize

image=cv.LoadImageM('4.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
binary_resize = imresize(image, (20,20))
binary_img = cv.fromarray(binary_resize)
cv.SaveImage('image.png', image) #Saves the image

cv.ShowImage('display',binary_img)
cv.WaitKey(10000)
