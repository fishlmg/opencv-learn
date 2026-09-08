import cv2
img=cv2.imread('./img/blur.jpg')
cv2.blur(img,(3,3))
img=cv2.boxFilter(img,-1,(3,3),normalize=True)


cv2.GaussianBlur(img,(3,3),3,3)
cv2.medianBlur(img,5)

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dx=cv2.Sobel(img,-1,1,0,ksize=3)#ddepth：处理结果图像深度，一般我们都填-1，即与原图深度相同。但在这里我们需要填写cv2.CV_64F。简单来说就是如果填写-1，我们在计算梯度时产生的负数就会被程序默认为0，导致有一边的边缘出不来。而cv2.CV_64F范围更大，可以保留负数。
cv2.convertScaleAbs(dx)#若像素值-255 < src * alpha + beta < 255，取绝对值；若像素值 alpha + beta >= 255 || src * alpha + beta <= -255,取255，不可溢出。
dy=cv2.Sobel(img,-1,0,1,ksize=3)
cv2.convertScaleAbs(dy)
mask=cv2.addWeighted(dx,0.5,dy,0.5,0)
cv2.imshow('a',mask)
cv2.waitKey()
