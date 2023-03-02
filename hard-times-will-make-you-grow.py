import random
import time
wait = time.sleep
def hardtimes():
    file = open("DepressionQuotes.txt")
    lines = file.readlines()
    for line in lines:
        print("_______________")
        print(line)
        wait(1)
hardtimes();