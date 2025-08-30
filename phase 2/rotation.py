import cv2 
#imported opencv version 2

image=cv2.imread('phase 2/sboy.webp')

if image is None:
    print("image not found ")
else: 
    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,180,0.5)
    rotated_image=cv2.warpAffine(image,M,(w,h))

    cv2.imshow("original image",image)
    cv2.imshow("rotated at 90 degrees",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
