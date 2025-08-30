import cv2 
#imported opencv version 2

image=cv2.imread('images\sboy.webp',cv2.IMREAD_GRAYSCALE)
#must be grayscale image

edges=cv2.Canny(image,50,150)

cv2.imshow("original image",image)
cv2.imshow(" edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()