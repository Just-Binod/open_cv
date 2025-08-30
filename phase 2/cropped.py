import cv2 
#imported opencv version 2

image=cv2.imread('images\sboy.webp')

if image is not None:
    cropped=image[100:200,50:150]
    cv2.imshow("original image",image)
    cv2.imshow("cropped image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




