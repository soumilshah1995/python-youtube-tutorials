'''
soumil shah
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

'''
import speech_recognition as sr
import pyttsx3
import time
import threading

def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('ready')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:
            command=r.recognize_google(audio).lower()
            print('You said: ' + command)
        except:
            print('Your last command could not be heard ! ')
            command = listen()
    return command

def assistant(command):
    if 'hello' in command:
        print('Ah you said hello')
        speak('small hello')
    elif 'Hello' in command:
        print('oh you said Hello')
        speak('Hello Saumil')
    elif 'what\'s up' in command:
        speak('Just doing my Thing')
    elif 'how are you' in command:
        speak('i am fine thanks for asking')
    else:
        speak('I dont know what you mean'+ command)

speak('i am ready for next commmands')
while True:
    t=threading.Thread(target=assistant(listen()), args=())
    t.start()
    # assistant(listen())






