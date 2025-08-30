import cv2 
#imported opencv version 2

image=cv2.imread('images\sboy.webp',cv2.IMREAD_GRAYSCALE)
#must be grayscale image

ret,thres_img=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("original image",image)
cv2.imshow(" Threshoded image",thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
we can try these value as threshold:
100,120,150
'''