import text_to_speech
import ai_text_generator
import speech_to_text

text = speech_to_text.generateText()
print(text)
response = ai_text_generator.generateResponse(text)
print(response)
text_to_speech.generateSpeech(response)
