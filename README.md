## 説明
Raspberry Pi 3 Model B上で画像撮影をしたあと、画像の前処理をほどこして学習と分類を行うためのライブラリです。
Data Augmentationにより100枚未満の比較的少ない画像からでも90%+の分類が行えます。
サンプルデータとして、フルーツの模型と日本の硬貨について学習した重み(.json, .h5)を同梱しています。

## Prerequisites
Raspbian Version 8.0系をインストールしたRaspberry Pi 3 Model Bが必要です。
OpenCV, and keras, sklearn subprocess embedded with Python 3.7のインストールもプログラムを動かすのに不可欠ですのでインストールしてください。
To fetch required components to make this work:
`pip install -r requirements.txt`

##　使い方
### camera.py 
```
python3 camera.py
```


## What does it stand for?
I want to take ownership of my learning with implementing something, or learn-by-doing.
This app enables you guys to change your raspberry pi into a camera image acquisition and object detection device!
