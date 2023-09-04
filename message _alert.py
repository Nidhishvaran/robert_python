import pyttsx3
from pyautogui import locateCenterOnScreen ,alert,click,moveTo,locateOnScreen
import speech_recognition as sr

mic = sr.Microphone()
listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print('listening..................')
            voice = listener.listen(source,timeout=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    
    
    except Exception as e:
        print(e)
        command = 'nothing'    
        
    return command   

def message():
    while  True:    
        minimize = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/min_mid.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        my = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/new_msg.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        if my:
            talk('sir you have one new message')
            command = get_command()
            if 'open it' in command:
                talk('ok sir')   
                click(my)
                click(minimize)
                break     
        else:
            pass

while True:
    message()
