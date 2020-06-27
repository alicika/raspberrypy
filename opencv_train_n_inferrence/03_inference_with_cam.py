
import cv2
import numpy as np
import keras
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array, load_img

#===================================================
#モデル、重み、学習プロセスの読み込み
#===================================================
#モデルを読み込む
model = model_from_json(open('model_fruits.json').read())

#重みを読み込む
model.load_weights('weights_fruits.h5')

#損失関数、オプティマイザを指定
model.compile(loss='categorical_crossentropy', optimizer='adam')


cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break
        
    #===================================================
    #推論する画像を読み込み
    #===================================================
    x = frame
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB) #RBGをRGBに変える
    x = cv2.resize(x, (32,32))

    #データ形式をCNNモデルに合わせる（3次元のPILから3次元のndarrayへ変更）
    x = img_to_array(x)

    #データを0.0～1.0へ正規化
    x = x.astype('float32')/ 255.0

    #次元を合わせる
    x = np.expand_dims(x, axis=0)

    #===================================================
    #推論と結果表示
    #===================================================
    #推論
    preds = model.predict(x)
    print("predicts : " + str(preds))

    #predsのインデックスでソート
    preds_argsort = np.argsort(preds)
    print("sort : " + str(preds_argsort))

    #最大のインデックス
    index = preds_argsort[0][-1]
    print("index(max) : " + str(index))

    #推論結果をリストから表示
    label_list = ["無し", "チェリー", "桃", "いちご"]
    print("予測 : " +str(label_list[index]))

    #推論結果の確率を表示
    probability = preds[0][index] * 100
    print("確率 : " + str(probability) + " %")    
 
cap.release()
cv2.destroyAllWindows()