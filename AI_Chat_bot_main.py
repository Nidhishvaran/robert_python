import subprocess
import os
from tkinter import Image 
from pyautogui import locateCenterOnScreen,click,moveTo,alert,locateAllOnScreen,screenshot
from keyboard import write,press_and_release
from datetime import datetime
from pyttsx3 import init
import numpy as np
import cv2
import time



engine = init()
        
def talk(text):
    engine.say(text)
    engine.runAndWait()

def reply(msg):
    click1 = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/svidhyaagiri.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
    text= locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/text_message.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
    click(text)
    write(msg)
    press_and_release('enter')
    click(click1)

subprocess.call('C:/Users/hp/AppData/Local/WhatsApp/WhatsApp')    

def wish():
    hour = int(datetime.now().hour)

    if hour>=0 and hour<12:
        reply('good morning sir/mam')
        
    elif hour>=12 and hour<18:
        reply('good afternoon sir/mam')
        
    else:
        reply('good evening sir/mam')
        


#alert('Sir now I am in active')  
'''click1 = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/svidhyaagiri.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
click(click1)'''
def bot():
    while True:
        
        good_morning = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/good_mrng.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        #details_lap_name,clip,pictures,C:/Users/hp/Pictures/Screenshots
        Documents = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/Document_img.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        pictures = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/pictures.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        camera = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/cam.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        path =  locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/path.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        pin = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/clip.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        details = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/detail.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        my = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/details_lap_full_2.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        no = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/no_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        home = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/home_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        stricker = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/stricker_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        hi = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/hi_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        name = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/name_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        how = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/how_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        no_voice = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/mic_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        thankyou =  locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/thankyou_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        can_i_get_your_details = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/details_lap_2.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        ok = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/ok_lap_reply.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70)
        what_are_the_policies_available_for_me = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/plans_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        i_want_to_take_lic = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/takelic_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        who_are_you =  locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/who_2.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        amma = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/amma_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        ok = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/ok_lap_2.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        can_i_call_you = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/call_lap.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        #cotact_me
        contact_me = locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/cotact_me.png',region = (0,0,1920,1080),grayscale = True, confidence=0.70) 
        
        if ok:
            click(ok) 
            reply("ok sir/mam thankyou for choosing me\nask like [don't use the numbers]1)I want to take lic,2)What are the plans available for me,3)Can I get your details,4)can I come to your office [write caps small and symbols like in menu]")
             
        elif who_are_you:
            click(who_are_you)
            reply('I am the AI bot of S.Dhaknalakshmi')
            
        elif details:
            click(details)
            reply("ok sir/mam thankyou for your Information")
          
                                                           
        elif i_want_to_take_lic :
            click(i_want_to_take_lic)                                  
            reply('ok contact me 9443372422\ncan I get your details\n[please send your details in this format]My details:\t\t\t\t\t\t\tie.your name, your age, your address,etc. ')
            
            
            
        
        elif what_are_the_policies_available_for_me:
            click(what_are_the_policies_available_for_me)
            reply('sir/mam go to our official website and check licindia.in \nif you have any doubts call me 9443372422')
            break
        
        elif no_voice:
            #talk('many of them are sending voice messages')
            click(no_voice)
            reply('please send text message because I am AI')
            
        elif can_i_get_your_details:
            #alert('sir someone asking for your details can i gave him')
            click(can_i_get_your_details)
            reply('I am S.Dhanalakshmi,\nI have more than twenty years of experience\nfor more info contact me\n9443372422')
        
        elif can_i_call_you :
            click(can_i_call_you)
            reply('yeah sure call between 9am-7pm \n my contact number is +91 9443372422')
            
        elif contact_me :
            click(contact_me)
            reply('yeah sure call between 9am-7pm \n my contact number is +91 9443372422')
            
        elif ok:
            click(ok)
            reply("what? please message like menu")
        
        elif stricker:
            click(stricker)
            reply('please send text message')
        
        elif home:
            click(home)
            reply('yeah sure\nmy office is in puduvayal,karaikudi,tamilnadu,india.\nfor more details call me 9443372422')
        
        
        
        elif thankyou:
            click(thankyou)
            reply("it's ok did you want any help from me")
            break   
        
        elif good_morning:
            click(good_morning)
            reply("good morning sir/mam , \n how can I help you ?")      
        
        

        
                        
        else:     
            pass                
while True:
    bot()    
    
'''elif details:
            
            click(details)
            time.sleep(1)
            img_name = "image_lic"
            var = screenshot()
            var = cv2.cvtColor(np.array(var),
                     cv2.COLOR_RGB2BGR)
            cv2.imwrite("C:/Users/hp/Documents/"+img_name+".png",var)
            reply("ok thankyou for your information don't share your details with others please onlyu share with the contact number +91 9443372422 ")
            amma = locateCenterOnScreen("C:/Users/hp/Pictures/kali linux/python application demo/amma_lic_dhanam.png",region = (0,0,1920,1080),grayscale = True,confidence = 0.70)
            while True:    
                if amma:
                    click(amma)
                    break
                else:
                    pass
            reply('we have new client!')
            while True:
                if amma:
                    click(amma)
                    break
                else:
                    pass
            while True:
                if pin:
                    click(pin)
                    print("pin")
                    break
                else:
                    pass
                
            press_and_release("up arrow")
            press_and_release("up arrow")
            press_and_release("enter")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("up arrow")
            press_and_release("up arrow")
            press_and_release("up arrow")
            press_and_release("up arrow")
            press_and_release("enter")
            press_and_release("tab")
            press_and_release("tab")
            press_and_release("tab")
            write(img_name)
            press_and_release("enter")
            press_and_release("enter")
            os.remove("C:/Users/hp/Documents/"+img_name+".png")
            
            #write(img_name)
            press_and_release("enter")'''
            
        
                                                         
            



















































































































































































































































































































































































































         
            
        

