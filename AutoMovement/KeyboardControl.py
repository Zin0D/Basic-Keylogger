from pynput.keyboard import Key, Controller
import time
import threading

print("Time To Launch GUI aswell")

keyboard = Controller()

def sleep(time_to_sleep):
    time.sleep(time_to_sleep)
    

def start_moving():
    keyboard.press('W')
    keyboard.release('W')
    sleep(3)
    keyboard.press('S')
    keyboard.release('S')
    sleep(3)

def check_dead():
    while True:
        if keyboard.pressed('O'):
            print("Oh") #Checking in a Seperate Thread but somehow buggin.
            return False
        time.sleep(1)

check = threading.Thread(target=check_dead, args=())
check.start()

if __name__ == "__main__":
    try:
        while check:
            start_moving()
        print("Exiting")
    except KeyboardInterrupt:
        print("Recognized Exit Signal, exiting...")

