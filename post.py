import webbrowser
import pyautogui
import time

chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
url = "https://api.whatsapp.com/send?phone="+"919578413023"+"&text="+"HareRama!"
webbrowser.get(chromedir).open(url)

time.sleep(2)
pyautogui.keyDown('alt')  # hold down the alt key
pyautogui.keyDown('space')
pyautogui.press('x')
pyautogui.keyUp('shift')    # release the space key
pyautogui.keyUp('alt')    # release the alt key
