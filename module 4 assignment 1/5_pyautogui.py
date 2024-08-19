import pyautogui
# from time import sleep
# sleep(5)
n = int(input())

for i in range(n):
    pyramid = "#" * (i + 1)
    pyautogui.write(pyramid)
    pyautogui.press('enter')

