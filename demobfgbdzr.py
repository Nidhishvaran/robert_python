import subprocess
import keyboard
from PIL import Image
import os

# Python program to take
# screenshots
  
  
import numpy as np
import cv2
import pyautogui
from time import sleep 
#sleep(3) 
# take screenshot using pyautogui
image = pyautogui.screenshot()
   
# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
   
# writing it to the disk using opencv
#cv2.imwrite("C:/Users/hp/Documents/image21378605657894.png", image)
#os.remove("C:/Users/hp/Documents/image213786056578945.png")
#subprocess.call("C:/Users/hp/Pictures/Screenshots/demo.png")
