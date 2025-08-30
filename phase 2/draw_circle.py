import cv2 
#imported opencv version 2

image=cv2.imread('phase 2/sboy.webp')

if image is None:
    print("image not found ")
else: 
       print("image loaded")

       cv2.circle(image, (200,200), 200, (0,0,254), 1)
       cv2.imshow("circled  image",image)
       cv2.waitKey(0)
       cv2.destroyAllWindows()


        

