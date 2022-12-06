import pyautogui
import time
import pyperclip

class Access:

  
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def click(self, cliks=1,button='left', pause=1):
    pyautogui.click(self.x, self.y, clicks=cliks,button=button, pause=pause)

if __name__ == "__main__":

  pyautogui.click(759,877,duration=3)

  pyautogui.click(597,107,duration=3)
  time.sleep(10)
  pyautogui.click(93,628,duration=3)

  pyautogui.click(278,222,duration=3)

  pyautogui.click(550,784,duration=3)

  pyperclip.copy("pyautoguiで送付しています ※class化")
  pyautogui.hotkey('ctrl', 'v')

  pyautogui.click(940,797,duration=3)
