import cv2
 
img = cv2.imread("image/strawberry1920x1080.jpg")
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
