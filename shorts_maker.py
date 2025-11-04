import pyautogui
import time

input("Press Enter")
time.sleep(1)
current_x, current_y = pyautogui.position()
print(current_x, current_y)