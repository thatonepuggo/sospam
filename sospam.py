import pyautogui
import time
import pydirectinput

prompt = pyautogui.prompt('Type in string to typewrite out.')
input2 = pyautogui.prompt('Press to open chat')
delay = pyautogui.prompt('Delay time. 0 for no delay (obviously)')

while(True):
	pyautogui.press(input2[:1])
	pyautogui.typewrite(prompt)
	pydirectinput.press('enter')
	print('Printed')
	time.sleep(float(delay))