from time import strftime
from sys import platform
import time
import os

if platform == "darwin":
    while True:
        tick = strftime('%I:%M:%S %p')

        print(f"Time: {tick}")
        time.sleep(1)
        os.system('clear')
else:
    while True:
        tick = strftime('%I:%M:%S %p')

        print(f"Time: {tick}")
        time.sleep(1)
        os.system('cls')