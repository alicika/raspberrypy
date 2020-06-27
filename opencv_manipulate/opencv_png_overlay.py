import cv2
from pngoverlay import PNGOverlay

#背景画像
dst = cv2.imread('image/cat.png')

#オーバーレイ画像
jellyfish = PNGOverlay('image/kurage_100px.png')

#オーバーレイ
jellyfish.show(dst, 430, 110) #x, yは表示したい中心座標

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()