from time import strftime
from sys import platform
import time
import os

if platform == "darwin":
    while True:
        os.system("clear")
        tick = strftime('%I:%M:%S %p')

        print(f"Time: {tick}")
        time.sleep(1)
else:
    while True:
        os.system('cls')
        tick = strftime('%I:%M:%S %p')
        print(f"Time: {tick}")
        time.sleep(1)