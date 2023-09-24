from colorama import *
from sys import *
import matplotlib.pyplot as plt
from colorama import *
from sys import platform
import shutil
import string
import os
import time
import psutil
import ctypes

# color for the bar graph
colors = ['green', 
          'red', 
          'yellow']


# the quit array that will be used to quit any program that uses it
quit = ["QUIT",
        "Quit",
        "QUIT()"]

#colors for the program to see
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
ORANGE_Start = "\033[38;2;255;165;0m"
ORANGE_END = "\033[0m"
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL
NORMAL = Style.NORMAL 
DIM = Style.DIM
Gray = Fore.LIGHTBLACK_EX
CYAN = Fore.CYAN