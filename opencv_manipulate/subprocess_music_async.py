import subprocess

#wav 同期から非同期に変更
subprocess.Popen(['aplay', 'sound/robot.wav'])

#mp3
subprocess.run(['mpg321', 'sound/cat.mp3'])

print('end')
