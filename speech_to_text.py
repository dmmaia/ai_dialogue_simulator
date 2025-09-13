import speech_recognition as sr

speech_eng = sr.Recognizer()

def generateText():
    with sr.Microphone(device_index=13) as source:
        print("Say something!")
        speech_eng.adjust_for_ambient_noise(source)
        speech_eng.energy_threshold=1000
        audio = speech_eng.listen(source)

    try:
        print("Recognizing.......")
        text = speech_eng.recognize_google(audio, language="en")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")