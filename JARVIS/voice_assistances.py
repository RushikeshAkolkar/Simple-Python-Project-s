import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime
import pyjokes

def sptotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not UnderStand")

def texttospeech(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

texttospeech("Hello Aishwarya Babasaheb Akolkar")
#sptotext("Hello")
