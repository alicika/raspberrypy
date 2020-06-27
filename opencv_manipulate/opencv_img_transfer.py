import cv2

counter = 0 
cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = cap.read()
    text = "counter : " + str(counter)
    cv2.putText(frame, text, (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 100), 10)
    counter = counter + 1
    cv2.imshow("image", frame)
    key = cv2.waitKey(1)
    if key != -1:
        break
 
cap.release()
cv2.destroyAllWindows()