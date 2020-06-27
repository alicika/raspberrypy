import cv2
import numpy as np

def rectangle(frame, point1, point2, color, opacity):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    
    # 黒い長方形作成
    rect_fill = np.zeros((y2-y1, x2-x1, 3), np.uint8)
    
    # 塗りつぶす色を変更
    rect_fill[:] = color

    # 長方形と同じサイズのframeのROI 
    rect_frame = frame[y1:y2, x1:x2];

    # rect_frameとrect_fillを 1-opacity:opacity でブレンドし、rect_frameに保存
    cv2.addWeighted(rect_frame, 1 - opacity, rect_fill, opacity, 0, rect_frame);

if __name__ == '__main__':
    frame = cv2.imread('image/cat.png')

    rectangle(frame, (350, 230), (450, 300), (0, 255, 0), 0.3)
    
    rectangle(frame, (0, 490), (750, 550), (0, 0, 0), 0.6)
    cv2.putText(frame, "Cyber CAT", (480, 535), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    cv2.imshow('window', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()