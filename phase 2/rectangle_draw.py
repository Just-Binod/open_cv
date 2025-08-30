import cv2 
#imported opencv version 2

image=cv2.imread('phase 2/sboy.webp')

if image is None:
    print("image not found ")
else: 
       print("image loaded")
       pt1=(49,10)
       pt2=(420,400)
       color=(0,0,254)
       thickness=3
       cv2.rectangle(image,pt1,pt2,color,thickness)
       cv2.imshow("rectangel image",image)
       cv2.waitKey(0)
       cv2.destroyAllWindows()


        

