import pyautogui
import time
time.sleep(7)
count=0
while count<100:
 pyautogui.typewrite("Hello!")
 pyautogui.press("enter")
 count+=1