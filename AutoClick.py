import pyautogui
import time
##how many tasks you want to run ?
total = 4
n=0
while n < total:
    pos=pyautogui.locateCenterOnScreen('Capture.PNG')
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(2)
    pos=pyautogui.locateCenterOnScreen('Capture2.PNG')
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(2)    
    n=n+1
