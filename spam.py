import pyautogui
import time

message = "todd" #ganti aja stringnya
n = 500          #banyak n nya

time.sleep(5)

for i in range(n):
	pyautogui.typewrite(message + '\n')
