import pyautogui
import time
from time import sleep
time.sleep(3)
###########################
memberCount=6			  #
###########################
toTag=memberCount-1
for i in range(toTag):
	pyautogui.hotkey('shift','2')
	time.sleep(0.01)
	for index in range(i):
		pyautogui.press("down")		
	pyautogui.press("enter")
