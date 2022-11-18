import pyautogui
import time
import pyperclip

pyautogui.FAILSAFE = True

def pyautogui_move_and_click(x_position,y_position):
    pyautogui.moveTo(x_position,y_position,duration=3, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

pyautogui_move_and_click(759,877)
time.sleep(5)
pyautogui_move_and_click(597,107)
time.sleep(5)
pyautogui_move_and_click(93,628)
time.sleep(5)
pyautogui_move_and_click(278,222)
time.sleep(5)
pyautogui_move_and_click(550,784)
time.sleep(5)
pyperclip.copy("pyautoguiで送付しています")
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui_move_and_click(891,834)
