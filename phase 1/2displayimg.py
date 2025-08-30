#commenting for my better understanding

import cv2 
#imported opencv version 2

image=cv2.imread("animeboy.webp")
#  read image

if image is  not None:
     cv2.imshow("image showing",image)  #open window
     cv2.waitKey(0)    #wait for a key
     cv2.destroyAllWindows()  #close window
   
else:
     print(" could not load a   image !") 


