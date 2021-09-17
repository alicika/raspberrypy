import cv2

counter = 0 
cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = cap.read()
    cv2.imshow("image", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('p'):
        frame = cv2.resize(frame, (320, 240))
        filename = "photo%04d.jpg" % counter
        cv2.imwrite(filename, frame)
        counter = counter + 1
 
cap.release()
cv2.destroyAllWindows()