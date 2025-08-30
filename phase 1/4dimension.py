import cv2 
#imported opencv version 2

image=cv2.imread("animeboy.webp")
#  read image

if image is not None:
    h,w,c=image.shape
    print(f"image loaded :\n height : {h}\n width : {w}\n channels : {c}")
else:
    print("could not load image")