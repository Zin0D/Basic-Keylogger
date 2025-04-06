from pynput.keyboard import Key, Controller
from pynput.mouse import *
import time
import threading

print("Time To Launch GUI aswell")

keyboard = Controller()

mouse = Controller()


def sleep(time_to_sleep):
    time.sleep(time_to_sleep)
    

def start_moving():
    keyboard.press('W')
    keyboard.release('W')
    sleep(3)
    keyboard.press('S')
    keyboard.release('S')
    sleep(3)


if __name__ == "__main__":
    while True:
        mouse.click(button=Button.left)
        time.sleep(0.1) #Remove for full GangBang
        

