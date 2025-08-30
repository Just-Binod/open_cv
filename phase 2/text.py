import cv2 
#imported opencv version 2

image=cv2.imread('phase 2/sboy.webp')

if image is None:
    print("image not found ")
else: 
       print("image loaded")
       cv2.putText(image,"hello binod is this ",(50,300),cv2.FONT_HERSHEY_COMPLEX,1.3,(0,0,234),2)

       cv2.imshow("adding text image",image)
       cv2.waitKey(0)
       cv2.destroyAllWindows()


        

