import cv2

img1 = cv2.imread("image/black1920x1080.jpg")
img2 = cv2.imread("image/cherry1920x1080.jpg")
img3 = cv2.imread("image/peach1920x1080.jpg")
img4 = cv2.imread("image/strawberry1920x1080.jpg")

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("image", img1)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('1'):
        cv2.imshow("image", img1)
    elif key == ord('2'):
        cv2.imshow("image", img2)
    elif key == ord('3'):
        cv2.imshow("image", img3)
    elif key == ord('4'):
        cv2.imshow("image", img4)

cv2.destroyAllWindows()