import subprocess

#wav
subprocess.run(['aplay', 'sound/robot.wav'])

#mp3
subprocess.run(['mpg321', 'sound/cat.mp3'])

print('end')