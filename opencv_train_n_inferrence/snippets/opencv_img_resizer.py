import cv2

img = cv2.imread("cat.jpg")
img = cv2.resize(img, (200, 200))
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()