import speech_recognition as sr

speech_eng = sr.Recognizer()

def generateText():
    #microphone_names = sr.Microphone.list_microphone_names()
    #for i, name in enumerate(microphone_names):
        #print(f"Microphone {i}: {name}")
    with sr.Microphone(device_index=14) as source:
        print("Say something!")
        speech_eng.energy_threshold = 50
        speech_eng.dynamic_energy_threshold = False
        audio = speech_eng.listen(source)

    try:
        print("Recognizing.......")
        text = speech_eng.recognize_google(audio, language="en")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")