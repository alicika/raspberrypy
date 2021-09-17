import cv2

img = cv2.imread("cat.jpg")
cv2.imshow("image", img)
    
while True:
    key = cv2.waitKey(1000)
    print(key)

cv2.destroyAllWindows()