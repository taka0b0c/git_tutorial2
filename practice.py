import pyautogui
import time
import pyperclip
def pyautogui_move_and_click(x_position,y_position):
    pyautogui.moveTo(x_position,y_position)
    pyautogui.click()
pyautogui_move_and_click(759,877)
time.sleep(5)
pyautogui_move_and_click(597,107)
time.sleep(10)
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
