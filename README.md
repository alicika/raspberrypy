## 説明
Raspberry Pi 3 Model B上で画像撮影をしたあと、画像の前処理をほどこして機械学習/分類を行うためのライブラリです。  
Data Augmentationにより100枚未満の比較的少ない画像からでも90%+の分類が行えます。  
のちに説明しますが、お好きなデータを用いて機械学習を行うための機能も搭載しています。  
サンプルデータとして、日本の硬貨とフルーツの模型について学習できるモデルと、学習した重み(.json, .h5)を読み込み画像が何か推論するモデルを同梱しています。

## Prerequisites
Raspbian Version 8.0系をインストールしたRaspberry Pi 3 Model Bが必要です。  
OpenCV, and keras, sklearn subprocess embedded with Python 3.7もプログラムを動かすのに不可欠ですのでインストールしてください。  

## 使い方
### Quickstart: 推論
```
python3 03_image_classifier_for_coins.py
```
ランダムで選択された画像がどのコインに近いかを推論します。

```
python3 04_image_classifier_for_fruits.py
```
ランダムで選択された画像がどのフルーツに近いかを推論します。

### Quickstart: 学習
### 01_learning_coins.py  
コインのデータについて機械学習し`03_image_classifier_for_coins.py`で使う重みデータを吐き出すのに必要なモデルを定義しています。

### 02_learning_fruits.py
コインのデータについて機械学習し`04_image_classifier_for_fruits.py`で使う重みデータを吐き出すのに必要なモデルを定義しています。
### camera.py 
新たなデータを写真で撮影し、オリジナルデータとして使用・機械学習・推論する際に使用します。  
起動方法
```
python3 camera.py
```
でウィンドウが開きますので`p`で画像を撮影しフォルダに保存、`q`でウィンドウを閉じることができます。

```


## What does it stand for?
I want to take ownership of my learning with implementing something, or learn-by-doing.
This app enables you guys to change your raspberry pi into a camera image acquisition and object detection device!
