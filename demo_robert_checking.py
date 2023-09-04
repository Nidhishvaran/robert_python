import pyautogui
import subprocess

def send_text_message():
                subprocess.call('C:/Users/hp/AppData/Local/WhatsApp/WhatsApp')
                while True:
                    start =pyautogui.locateCenterOnScreen('C:/Users/hp/Pictures/kali linux/python application demo/search.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
                    if start:
                        break
                    else:
                        pass
                if start is not None:
                    pyautogui.moveTo(start)
                    pyautogui.click()
                    
send_text_message()