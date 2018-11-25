'''
soumil shah
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

'''

import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


print(r.recognize_google(audio))Q
speak(r.recognize_google(audio))




