import cv2
print(" welcome ")
ip=input("enter the location from you want image :   ")

#read / load the image from specific location
image=cv2.imread(ip)


#converting to gray scale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Create a named window with custom size
cv2.namedWindow("Grayscale image", cv2.WINDOW_NORMAL)  # Makes it resizable
cv2.resizeWindow("Grayscale image", 800, 600)  # Set width=800, height=600

# Show the image
#sa

print(f"_____enter 0 if you want to see image only ____")
print(f" ____enter 1 if you want to save____")

status=int((input("enter 0 or 1 : ")))
if status==0:
    cv2.imshow("Grayscale image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif status==1:
    location=input("enter location and name with extension to save your image: ")
    done=cv2.imwrite(location,gray)
    if done:
        print("image saved sucessfully at {location}")

else:
    print(f" Error , please choose either 0 or 1 !")

