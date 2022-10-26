from pynput import keyboard
import pyautogui

def get_key(key):
    print(key)
    print(pyautogui.position())
    if key == keyboard.Key.f12:
        print('F12 GO!')
        return False


with keyboard.Listener(on_press=get_key) as l:
    l.join()
