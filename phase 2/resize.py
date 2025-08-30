
import cv2 
#imported opencv version 2

image=cv2.imread('images\sekhar me posae.JPG')

if image is None:
    print("image not found ")
else: 
    print("image loaded")

    resized=cv2.resize(image,(300,300))
    #width,ht
    cv2.imshow("original image",resized)
    cv2.imwrite("resized_output.jpg",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
