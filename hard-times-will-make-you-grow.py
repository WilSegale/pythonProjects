import random
import time
import os

wait = time.sleep
def hardtimes():
    file = open("DepressionQuotes.txt",'r')
    lines = file.readlines()
    random.shuffle(lines)
    for line in lines:
        print(line)
        wait(5)
        os.system('clear')
hardtimes();