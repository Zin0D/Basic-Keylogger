from ctypes import *
from io import StringIO
from platform import architecture
import time

""" Self explanatory """
# Gets the PID of the current process.
def get_current_process():
    hwnd = windll.user32.GetForegroundWindow() #Returns PID of the currnent Application in the Foreground.
    pid = c_ulong(0)

    windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = f'{pid.value}'
    
    return process_id


""" Assign the Params , check for system_architecture"""
def checkos():

    if architecture()[0] == "64bit":
        lres = c_void_p
        ULONG_PTR = c_ulonglong

    else:
        lres = c_long
        ULONG_PTR = c_ulong
    
    return ULONG_PTR, lres


""" Prints PID """
def looped_gcp():
    while True:
        id = get_current_process()
        print(f"ID = {id}")
        time.sleep(5)

