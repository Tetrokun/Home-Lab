import os
import socket
import sys
from colored import fg, bg, attr
from pyfiglet import print_figlet

Hostname = socket.gethostname()
if os.name == 'nt':
    OS = "Windows"
elif os.name =='posix':
    OS = "Linux"
if OS=="Windows":
    print_figlet('Windows script',font="standard", colors='255;165;0:')
if OS=="Linux" :
    print_figlet('Linux Script',font="slant", colors='255;90;0:')
    print_figlet(Hostname,font="slant", colors='255;90;0:')







