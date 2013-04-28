import cv


grey=cv.LoadImage('1515.png', cv.CV_LOAD_IMAGE_GRAYSCALE) #Load the image

# create the wanted images
eig = cv.CreateImage (cv.GetSize (grey), 32, 1)
temp = cv.CreateImage (cv.GetSize (grey), 32, 1)


image = cv.CloneImage(grey)

# the default parameters
quality = 0.01
min_distance = 10
MAX_COUNT = 1000

# search the good points
features = cv.GoodFeaturesToTrack (
        grey, eig, temp,
        MAX_COUNT,
        quality, min_distance, None, 3, 0, 0.04)
for (x,y) in features:
    #print "Good feature a: "+str(x)+','+str(y)
    cv.Circle (image, (int(x), int(y)), 3, (0, 255, 0), -1, 8, 0)


cv.ShowImage('Good Feature',image)
cv.WaitKey(10000)
