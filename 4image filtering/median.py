import cv2 
#imported opencv version 2

image=cv2.imread('images\sboy.webp')

blurred=cv2.medianBlur(image,5)
cv2.imshow("original image",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()