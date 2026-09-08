import cv2
img=cv2.imread('./img/QRcode.webp')
codeinfo,points,straight_qrcode=cv2.QRCodeDetector().detectAndDecode(img)
print(points)
print(codeinfo)#content
print(straight_qrcode)#code