import time 
import random 
import pyautogui


def move_mouse():
    xsize, ysize = pyautogui.size()
    x, y = random.randrange(xsize), random.randrange(ysize)
    pyautogui.moveTo(x, y, duration=0.1)
    

def enable_caps():
    pyautogui.press('capslock')


def meta_key_modifer_press():
    mod = [
        "left",
        "right",
        "up",
        "down",
        "m",
        "v",
        "a",
        "b",
        "c",
        "d",
        "i",
        ".",
        "home",
        "+",
        "-"
    ]
    num = random.randint(0, len(mod) -1) 
    pyautogui.hotkey("win", mod[int(num)])


if __name__ == "__main__":

    while True: 
        num = random.randint(0,3)
        if num == 0: 
            move_mouse()
        if num == 1:
            enable_caps()
        if num == 2:
            meta_key_modifer_press()
        if num == 3: 
            move_mouse()
        time.sleep(random.randint(1,300))


    