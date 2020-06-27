import cv2
 
img = cv2.imread("image/cat.jpg")
cv2.putText(img, "Please Don't Disturb.", (80, 530), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 8)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
