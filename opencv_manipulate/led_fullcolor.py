import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO16, 20, 21を出力端子設定
GPIO.setup(16, GPIO.OUT) #Red
GPIO.setup(20, GPIO.OUT) #Blue
GPIO.setup(21, GPIO.OUT) #Green

#Red
GPIO.output(16, 1) #Red
GPIO.output(20, 0) #Blue
GPIO.output(21, 0) #Green
time.sleep(2)

#Blue
GPIO.output(16, 0) #Red
GPIO.output(20, 1) #Blue
GPIO.output(21, 0) #Green
time.sleep(2)

#Green
GPIO.output(16, 0) #Red
GPIO.output(20, 0) #Blue
GPIO.output(21, 1) #Green
time.sleep(2)

#OFF
GPIO.output(16, 0) #Red
GPIO.output(20, 0) #Blue
GPIO.output(21, 0) #Green