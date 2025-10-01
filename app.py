import text_to_speech
import ai_text_generator
import speech_to_text
from os import listdir
import os

text = speech_to_text.generateText()
print(text)
response = ai_text_generator.generateResponse(text+"\n Response with 10 or less lines")
print(response)
plain_text = response.replace("*","").replace("\n", "")

i = 0
for phrase in plain_text.split("."):
    i+=1
    text_to_speech.generateSpeech(phrase,str(i))
    os.system("paplay midia/"+str(i)+".mp3")

for file in listdir("midia/"):
    os.remove("midia/"+file)
