import pyautogui
import time
import random


def interact(x, y):

    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    time.sleep(random.uniform(0.5, 1.5))
    pyautogui.press('j')

def first_cast(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.press('j')
