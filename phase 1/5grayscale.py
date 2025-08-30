import cv2 
#imported opencv version 2

image=cv2.imread("animeboy.webp")
#  read image

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #convert img into grayscale image
    cv2.imshow("grayscale image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #image show garna lai
else:
    print("sorry, couldnot load the image")