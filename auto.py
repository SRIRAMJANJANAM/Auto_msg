import pyautogui as gui
import time
msg=input('Enter message:')
num=input("Enter num:")
time.sleep(1)
for i in range(int(num)):
    gui.typewrite(msg)
    gui.press('Enter')