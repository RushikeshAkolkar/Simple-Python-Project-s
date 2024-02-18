import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime
import pyjokes
import os

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
            return data
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

if __name__ == '__main__':
        texttospeech("Good Morning I am JARVIS")

        while True:
          data1 = sptotext().lower()

          if "your name" in data1:
               name = "my name is rishikesh"
               texttospeech(name)

          elif "old are you" in data1:
               age = "i am 26 years old"
               texttospeech(age)

          elif 'time' in data1:
               time = datetime.datetime.now().strftime("%I%M%p")
               texttospeech(time)

          elif 'youtube' in data1:
               wb.open("https://www.youtube.com/watch?v=lnlB2ze0xZg")

          elif 'joke' in data1:
               joke_1 = pyjokes.get_joke(language="en", category="neutral")
               print(joke_1)
               texttospeech(joke_1)

          elif "exit" in data1:
               texttospeech("Thank you")
               break
