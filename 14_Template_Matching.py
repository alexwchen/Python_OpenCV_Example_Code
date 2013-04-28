import cv

# Original Image
image=cv.LoadImage('picture.png', cv.CV_LOAD_IMAGE_GRAYSCALE) #Load the image

# Get Template
cv.SetImageROI(image, (100,100,50,50))
template=cv.CloneImage(image)

cv.ShowImage("template",template)

cv.ResetImageROI(image)
W,H=cv.GetSize(image)
w,h=cv.GetSize(template)
width=W-w+1
height=H-h+1
result=cv.CreateImage((width,height),32,1)


# cv.CV_TM_SQDIFF means is a Least Square similarity match
# Probably not useful to use since we can do this ourselves
cv.MatchTemplate(image,template, result,cv.CV_TM_SQDIFF)


(min_x,max_y,minloc,maxloc)=cv.MinMaxLoc(result)
(x,y)=minloc


image2=cv.CloneImage(image)
cv.Rectangle(image2,(int(x),int(y)),(int(x)+w,int(y)+h),(255,255,255),1,0)


cv.ShowImage("Find Match",image2)

cv.WaitKey(10000)
