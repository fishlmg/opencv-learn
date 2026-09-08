import cv2
import numpy as np

img=cv2.imread('./img/corner.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img_gray=np.float32img_(gray)

corner=cv2.cornerHarris(img_gray,2,3,0.04)
img[corner>0.01*corner.max()]=(0,0,255)
cv2.imshow('a',img)
cv2.waitKey(0)
cv2.destroyAllWindows


