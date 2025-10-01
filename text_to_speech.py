from gtts import gTTS

lang = 'en'

def generateSpeech(text,name):
    audio = gTTS(text=text, lang=lang, tld="com")
    audio.save("midia/"+name+".mp3")