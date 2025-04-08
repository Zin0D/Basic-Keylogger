from pynput.keyboard import Key, Controller
from pynput.mouse import *
import time
import threading
import base64
import subprocess
import os


print("Time To Launch GUI aswell")

keyboard = Controller()

mouse = Controller()

payload = base64.b64encode(b"whoami") #Takes input as byte.
print(payload.decode())

def sleep(time_to_sleep) -> None:
    time.sleep(time_to_sleep)
    

def start_moving() -> None:
    keyboard.press('W')
    keyboard.release('W')
    sleep(3)
    keyboard.press('S')
    keyboard.release('S')
    sleep(3)


def on_clicking(time_double:float) -> None:
    print("This may Crash your pc, recommended Time in Seconds: 0.01 at fastest!\n You sure you want to continue?: [YES] [NO] ")
    if (input().lower() == "no"):
        exit(0)


    while True:
        mouse.click(button=Button.left)
        sleep(time_double)


#thrad_on = threading.Thread(target=on_clicking, args=()) #Ready?
#thrad_on.start() Fix why Thread not working

finalised_gregg = None


def cmd() -> str:
    return base64.b64decode(payload)
    #finalised_gregg += base64.decode(i)

if __name__ == "__main__": 
    #print("Staring AutoPressing.")
    
    try:
        on_clicking(0.01)
    except KeyboardInterrupt:
        print("Stopped Clicking.")

        
    try:
        subprocess.run(cmd().decode())
    except Exception as cooked:
        None
    print("Done.")
