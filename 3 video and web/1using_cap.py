import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()   #ret= t/f and frame=image

    if not ret:
        print("couldnot read frame !")
        break
    cv2.imshow("webcam feed ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(".... QUITTING.....")
        break
cap.release()
cv2.destroyAllWindows()



# @@


