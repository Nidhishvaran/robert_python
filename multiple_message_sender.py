from datetime import datetime
import subprocess
from pyautogui import locateCenterOnScreen,alert,click,moveTo
from keyboard import write,press_and_release




def reply(person,msg):
    subprocess.call('C:/Users/hp/AppData/Local/WhatsApp/WhatsApp')
    while True:
        search = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/search.png',region=(0,0,1090,1080),grayscale = True,confidence = 0.70)
        if search:
            click(search)
            write(person)
            press_and_release('enter')
            break
        else:
            pass

    while True:
        text = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/text_message_lap.png',region=(0,0,1920,1080),grayscale = True,confidence=0.70)
        if text:
            click(text)
            write(msg)
            press_and_release('enter')
            break
        else:
            pass
        
def wish():
    today = str(datetime.today())
    if '03-16' in today:
        reply('amma','how are you')
    elif '01-26' in today:
        reply('amma lic','happy birthday nikhil')
    elif '05-05' in today:
        reply('amma lic','hi')
        reply('surya','hi ')
        reply('selva','selva! selva! selva!')
        reply('sornaganesh','hi bro')
        reply('hamsa','enna panra')
        #reply('natraj 2','hi')
        reply('deva new','hi')
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()    
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    elif '' in today:
        reply()
    else:
        pass
    
wish()
        


            
             
    

     
    
     