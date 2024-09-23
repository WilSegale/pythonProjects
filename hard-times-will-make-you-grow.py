import random
import time
import os

wait = time.sleep
def hardtimes():
    file = open("DepressionQuotes.txt",'r')
    lines = file.readlines()
    random.shuffle(lines)
    for line in lines:
        print(f"{line}")
        wait(1)
hardtimes()