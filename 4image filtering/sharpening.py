import cv2 
#imported opencv version 2
import numpy as np

image=cv2.imread('images\sboy.webp')
sharpen_kernal=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]

])

sharpened=cv2.filter2D(image,-1,sharpen_kernal)
cv2.imshow("original image",image)
cv2.imshow("blurred image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()