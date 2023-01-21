from time import strftime
import time
import os

while True:
    tick = strftime('%H:%M:%S %p')
    print(f"Time: {tick}")
    time.sleep(1)
    os.system('clear')