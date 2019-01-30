import os
import socket
import platform
from art import *
from termcolor import colored
from colorama import *
init()
Hostname = socket.gethostname()
if os.name == 'nt':
    OS = "Windows"
elif os.name =='posix':
    OS = "Linux"

tprint(colored(Hostname, 'green', 'on_red'))



