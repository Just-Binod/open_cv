import cv2 
#imported opencv version 2

image=cv2.imread('phase 2/sboy.webp')

if image is None:
    print("image not found ")
else: 
    flip_horizontal=cv2.flip(image,1)
    flip_vertical=cv2.flip(image,0)
    flip_both=cv2.flip(image,-1)

    cv2.imshow("original",image)
    cv2.imshow("hori",flip_horizontal)
    cv2.imshow("vert",flip_vertical)
    cv2.imshow("both",flip_both)
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()

