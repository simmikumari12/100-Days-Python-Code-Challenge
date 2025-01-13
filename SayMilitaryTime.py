import sys
from gtts import gTTS
from preferredsoundplayer import soundplay

military_time = sys.argv[1]
accent = sys.argv[2]
if len(sys.argv) > 3:
    print("Too many arguments!")