import cv2

template=cv2.imread('./img/template.jpg')
img=cv2.imread('./img/crowd.jpg')
h,w,l=template.shape
res=cv2.matchTemplate(img,template,cv2.TM_CCOEFF)#相关系数
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
top_left=max_loc
bottom_right=(top_left[0]+w,top_left[1]+h)
cv2.rectangle(img,top_left,bottom_right,(255,255,0),2)
cv2.imshow('a',img)
cv2.waitKey(0)