import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def putText_japanese(img, text, point, size, color):
    #Notoフォントとする
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', size)

    #imgをndarrayからPILに変換
    img_pil = Image.fromarray(img)
    
    #drawインスタンス生成
    draw = ImageDraw.Draw(img_pil)
    
    #テキスト描画
    draw.text(point, text, fill=color, font=font)

    #PILからndarrayに変換して返す
    return np.array(img_pil)
    
if __name__ == '__main__':
    img= cv2.imread("image/cat.png")
    
    # cv2.putTextのフォントサイズとはスケールが異なるので注意
    img = putText_japanese(img, "吾輩は猫である", (50, 450), 100, (25, 131, 255))

    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()