import json
import shutil
from colorama import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import shutil
from colorama import *
from sys import platform
import string

GREEN = Fore.GREEN
RESET = Fore.RESET
total, used, free = shutil.disk_usage("/")
import platform
import string
from ctypes import windll

def get_drives():
    if platform.system() == "Windows":
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1

        return drives

print(f"Drives: {get_drives()}")  # This will print the list of available drives on Windows
drives = input(">>> ")


data = {
    f"DiskSpace for {drives}":[
        {"Total-GB": total // (2 ** 30)}, 
        {"Used-GB": used // (2 ** 30)},
        {"Free-GB":(free // (2 ** 30))}
    ]}
json_data = json.dumps(data,indent=2)

with open("DiskSpace.json", "w") as outfile:
    outfile.write(json_data)
print(f'{GREEN}Done. It is located in the file called: DiskSpace.json{RESET}')
get_drives()