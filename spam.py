import pyautogui
import time

message = "todd" #ganti aja stringnya
n = 500          #banyak n nya

print("\nSTART")

time.sleep(5)

print("\n COMPLETE")

for i in range(0, int(n)):
	pyautogui.typewrite(message + '\n')

