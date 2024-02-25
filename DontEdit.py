from sys import *
from sys import platform
import pkg_resources
import subprocess
import matplotlib.pyplot as plt
import platform
import json
import shutil
import string
import os
import time
import psutil
import ctypes
import socket

# the quit array that will be used to quit any program that uses it
quit = ["QUIT", "Quit", "QUIT()", "quit", "quit()",
        "Exit", "exit", "EXIT"]

# yes or no array so if the user wants to have something with a yes it output it to something and the opeset for the other one
no = ["no", "NO", "No", "N", "n"]
yes = ["yes", "YES", "Yes", "Y", "y"]
Install = ["install", "INSTALL", "Install", "i", "I","in","IN"]
Uninstall = ["uninstall", "UNINSTALL", "Uninstall", "u", "U","un","UN"]
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[0m"]

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
ORANGE_Start = "\033[38;2;255;165;0m"
ORANGE_END = "\033[0m"
BRIGHT = "\033[1m"
RESET = "\033[0m"
GRAY_TEXT = "\033[90m"
CYAN_TEXT = "\033[36m"