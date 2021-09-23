## 説明
Raspberry Pi 3 Model B上で画像撮影をしたあと、画像の前処理をほどこしてから機械学習で画像識別を行うためのライブラリです。  
Data Augmentationにより100枚未満の比較的少ない画像からでも90%+の分類が行えます。  
のちに説明しますがカメラで対象を撮影してデータを作成し、それを用いて機械学習を行うための機能も搭載しています。  
サンプルデータとして日本の硬貨およびフルーツの模型について学習できるモデルと、学習した重み(.json, .h5)を読み込み画像を識別できるモデルを同梱しています。

## Prerequisites
Raspbian Version 8.0系をインストールしたRaspberry Pi 3 Model Bにて動作検証しています。  
OpenCVでカメラを用いたウィンドウを使用しますので、カメラの接続が必要です。  
OpenCV, and keras, sklearn subprocess embedded with Python 3.7もプログラムを動かすのに不可欠ですのでインストールしてください。  
学習に使用する画像データはバイナリデータですのでgitで管理していません。[コイン画像](https://drive.google.com/file/d/12nX8mnAh-ezWVv1YXOXh3ZAOMGQubEuY/view?usp=sharing, "コイン画像"), [フルーツ画像](https://drive.google.com/file/d/1DQ8IT7K2zH5weZfMS3n5fRtWyCHdRsWt/view?usp=sharing, "フルーツ画像")からDLし、ディレクトリを当ファイルと同じ階層に配置してください。

## 使い方
### Quickstart:
学習済みモデルを同梱していますので、コインとフルーツについて識別するだけであれば`03_image_classifier_for_coins.py`および`04_image_classifier_for_fruits.py`をそのまま使用できます。  
コインとフルーツの判別機能について説明します。
```
python3 03_image_classifier_for_coins.py
```
撮影中の画像がどのコインに近いかを推論します。

```
python3 04_image_classifier_for_fruits.py
```
撮影中の画像がどのフルーツに近いかを推論します。

### 学習
パラメータを変更しての追加学習やオリジナルデータでの画像識別に必要です。  
画像をDLし、それぞれのプログラムと同じ階層に学習したい画像を入れたディレクトリが必要になります。  
コインとフルーツについて識別するだけであれば`01_learning_coins.py`および`02_learning_fruits.py`をそのまま使用できます。  

### 01_learning_coins.py  
コインのデータについて機械学習し`03_image_classifier_for_coins.py`で使う学習済みモデルを吐き出すのに必要な機械学習フローを定義しています。

### 02_learning_fruits.py
フルーツのデータについて機械学習し`04_image_classifier_for_fruits.py`で使う学習済みモデルを吐き出すのに必要な機械学習フローを定義しています。

## オリジナルデータ作成
### camera.py 
新たなデータを写真で撮影し、オリジナルデータとして使用・機械学習・推論する際に使用します。  
起動方法
```
python3 camera.py
```
でウィンドウが開きますので`p`で画像を撮影しフォルダに保存、`q`でウィンドウを閉じることができます。

## 変更できるパラメータ 
コメント行で`#★`のついたパラメータを変更することでオリジナルデータの機械学習・オリジナルデータでの画像識別が可能です。 
推論モデル: `model`, `model.load_weights`, `label_list`  
学習モデル: `list_folder`, `epochs_num`, `batch_size_num`, `model_coin.json`, `model.save_weights`   

## What does it stand for?
I want to take ownership of my learning with implementing something, or learn-by-doing.
This app enables you guys to change your raspberry pi into a camera image acquisition and object detection device!
