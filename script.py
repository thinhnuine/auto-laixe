import pyautogui
import time
import datetime
import subprocess


POPUP_IMAGE = "popup.png"


# focus Brave
def focus_brave():

    subprocess.run([
        "osascript",
        "-e",
        'tell application "Brave Browser" to activate'
    ])


# reload tab
def reload_page():

    subprocess.run([
        "osascript",
        "-e",
        '''
        tell application "Brave Browser"
            activate
            tell application "System Events"
                keystroke "r" using command down
            end tell
        end tell
        '''
    ])

    print("Đã reload")


# click giữa màn hình
def click_center():

    width, height = pyautogui.size()

    x = width // 2
    y = height // 2

    pyautogui.click(x, y)

    print("Đã click giữa màn hình")


# check popup
def check_popup():

    try:

        location = pyautogui.locateOnScreen(
            POPUP_IMAGE,
            confidence=0.7,
            grayscale=True
        )

        if location:

            focus_brave()

            time.sleep(0.5)

            click_center()

            time.sleep(2)

    except pyautogui.ImageNotFoundException:

        pass


# check reload time
def check_reload():

    now = datetime.datetime.now()

    if now.hour == 0 and now.minute == 5:

        reload_page()

        time.sleep(60)


# main loop
print("Script started")

time.sleep(3)


while True:

    time.sleep(10)

    check_popup()

    check_reload()

    time.sleep(1)