
from DontEdit import os,time,random
wait = time.sleep
def hardtimes():
    file = open("DepressionQuotes.txt",'r')
    lines = file.readlines()
    random.shuffle(lines)
    for line in lines:
        print(line)
        wait(1)
hardtimes();