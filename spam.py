import pyautogui
import time

message = "todd" #ganti aja stringnya
n = 500          #banyak n nya

print("\nSTART")

count = 5
while(count != 0) :
	time.sleep(1)
	count -= 1

print("\n COMPLETE")

for i in range(0, int(n)):
	pyautogui.typewrite(message + '\n')

