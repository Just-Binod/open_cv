import cv2 
#imported opencv version 2

image=cv2.imread("animeboy.webp")
#  read image

if image is not None:
    success=cv2.imwrite("output.webp",image)
    if success:
        print("image saved sucessfuly as -- output.webp -- ")
    else:
        print("failed to save an image")
else:
    print("error , couldnot load image")
