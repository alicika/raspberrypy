import cv2
import subprocess

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
        subprocess.Popen(['mpg321', 'sound/camera-shutter3.mp3'])
        counter = counter + 1
 
cap.release()
cv2.destroyAllWindows()
