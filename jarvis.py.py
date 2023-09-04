import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init() 

def talk():
    engine.say()
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening..........')
        voice = listener(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        if "youtube" in command:
            print(command)
except:
    pass