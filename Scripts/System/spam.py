import pyautogui
import time
print("You have 5 seconds to switch to the tab and select the chat where you want to spam the message")
time.sleep(5)
f = open("spamtext.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
