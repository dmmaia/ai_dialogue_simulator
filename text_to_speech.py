from gtts import gTTS

import os

lang = 'en'

def generateSpeech(text):
    audio = gTTS(text=text, lang=lang, tld="com")
    audio.save("midia/speech.mp3")
    os.system("paplay midia/speech.mp3")