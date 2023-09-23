# Clears all timers
from DontEdit import *

if platform == "darwin" or platform == "linux":
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