from pynput.keyboard import Controller, Listener
import pyautogui


def findCords():
    cords = pyautogui.locateCenterOnScreen("GoldCrown.png")
    return cords


def check_key_press(key):
    try:
        if key.vk == 96:
            crown = findCords()
            pyautogui.moveTo(crown)
            print(crown)
            return False
    except AttributeError:
        print("Not good press")

with Listener(on_press=check_key_press) as l:
    l.join()
