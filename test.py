import vlc
from time import sleep
p = vlc.MediaPlayer("01. Thundertruck.mp3")
print p
p.play()
sleep(5)
