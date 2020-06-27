import random
import subprocess

weather_list = ["晴れ", "くもり", "雨"] 
weather = random.randint(0, 2)
rain = random.randint(0, 100)

text1 = "明日の天気は" + weather_list[weather] + "です"
text2 = "降水確率は" + str(rain) + "%です"

subprocess.run(['./jtalk.sh', text1])
subprocess.run(['./jtalk.sh', text2])