#commenting for my better understanding

import cv2 
#imported opencv version 2

image=cv2.imread("animeboy.webp")
 #  read image

if image is None:
    print("ERROR ! image not found")
else:
     print(" Image Loaded  sucessfully") 
#normal if _else condition to check if image is loaded or not

