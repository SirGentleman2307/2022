from pynput.keyboard import Controller, Listener
from csv import reader
import pyautogui
import time

codes = []

# Global button position to be cailabrated
TextBox = [1275, 1080]
SubmitBox = [1280, 1180]
ClaimBox = [1945, 1175]
XBox = [2300, 285]
ErrorBox = [1720, 815]

with open('Export (6).csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        key = ''.join(row[1].split('-'))
        codes.append(key)


def input_code():
    keyboard = Controller()
    for i in range(1, len(codes)):
        # move and click the text box
        pyautogui.click(TextBox[0], TextBox[1])
        # type in the code
        keyboard.type(codes[i])
        time.sleep(0.25)
        # move and click the submit
        pyautogui.click(SubmitBox[0], SubmitBox[1])
        time.sleep(0.3)

        # IF ERROR THEN CLICK CONTINUE BUTTON
        pyautogui.click(ErrorBox[0], ErrorBox[1])
        time.sleep(0.3)

        if i % 5 == 0:
            # move and click the claim
            pyautogui.click(ClaimBox[0], ClaimBox[1])
            time.sleep(1.5)
            # move and click the X
            pyautogui.click(XBox[0], XBox[1])
            time.sleep(0.25)
            pyautogui.click(XBox[0], XBox[1])
            time.sleep(0.75)
            print(codes[i])

    # move and click the claim
    pyautogui.click(ClaimBox[0], ClaimBox[1])
    time.sleep(1.5)
    # move and click the X
    pyautogui.click(XBox[0], XBox[1])
    time.sleep(0.25)
    pyautogui.click(XBox[0], XBox[1])
    time.sleep(0.75)

# TO DO
def claibate_keys():
    pass

def check_key_press(key):
    if key.vk == 96:
        return False

    if key.vk == 97:
        # Submit (Num 1)
        pyautogui.moveTo(1280, 1180)

    if key.vk == 98:
        # Enter (Num 2)
        pyautogui.moveTo(1275, 1080)

    if key.vk == 99:
        # Claim (Num 3)
        pyautogui.moveTo(1945, 1175)

    if key.vk == 100:
        # X (Num 4)
        pyautogui.moveTo(2300, 285)

    if key.vk == 101:
        # Start (Num 5)
        time.sleep(1)
        input_code()
        return False

    print(key)
    print(pyautogui.position())


with Listener(on_press=check_key_press) as l:
    l.join()
