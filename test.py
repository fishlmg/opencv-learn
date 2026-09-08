import cv2
img=cv2.imread('1.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,img_thresh=cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("a",img_thresh)
cv2.waitKey()

points,_=cv2.findContours(img_thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for contour in points:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)

cv2.drawContours(img_thresh,approx,-1,(0,0,255),2,1)
cv2.imshow("a",img_thresh)
cv2.waitKey()
if len(points)==2:
    areas=[]
    for i in range(2):
        area=cv2.contourArea(points[i])
        areas.append(area)
    print(areas)
else:
    print(len(points))
