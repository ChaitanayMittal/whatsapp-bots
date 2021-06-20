import pyautogui
import time
from time import sleep
time.sleep(3)
spamString = "enter your spam message"
#f = open("bulleya_lyrics.txt", 'r')
#for word in f:
for x in range(35):
	pyautogui.typewrite(spamString)
	time.sleep(0.1)
	pyautogui.press("enter")
	# pyautogui.press("enter")
	
	
	
