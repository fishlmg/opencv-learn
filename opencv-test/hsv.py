import cv2
import numpy as np

img=cv2.imread('./img/opencv.jpg')
im_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('hsv',im_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

red_l1=np.array([[0,43,46]])
red_h1=np.array([[10,255,255]])
red_l2=np.array([[156,43,36]])
red_h2=np.array([[180,255,255]])

mask1=cv2.inRange(im_hsv,red_l1,red_h1)# mask1 为二值图像
mask2=cv2.inRange(im_hsv,red_l2,red_h2)

red1=cv2.bitwise_and(im_hsv,im_hsv,mask=mask1)
red2=cv2.bitwise_and(im_hsv,im_hsv,mask=mask2)
red=cv2.bitwise_or(red1,red2)
red=cv2.cvtColor(red,cv2.COLOR_HSV2BGR)
cv2.imshow('red',red)
cv2.waitKey(0)
cv2.destroyAllWindows
