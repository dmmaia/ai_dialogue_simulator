from gtts import gTTS

import os

text = "Simple test response"
lang = 'en'

audio = gTTS(text=text, lang=lang, tld="com")
audio.save("midia/test.mp3")
os.system("paplay midia/test.mp3")