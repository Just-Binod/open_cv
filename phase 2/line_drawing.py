
import cv2 
#imported opencv version 2

image=cv2.imread('images\sekhar me posae.JPG')

if image is None:
    print("image not found ")
else: 
    print("image loaded")

    pt1=(50,100)
    pt2=(300,200)

    color=(255,0,0)
    thickness=4

    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("line draw",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



