import json
import shutil
import string
from colorama import *
from sys import platform

GREEN = Fore.GREEN
RESET = Fore.RESET
if platform == "win32":
    from ctypes import windll
    def get_drives():
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1

        return drives

    if __name__ == '__main__':
        print(f"drive: {get_drives()}")   # On my PC, this prints ['A', 'C', 'D', 'F', 'H']

drive = input(f"Drive: ")
total, used, free = shutil.disk_usage(f"{drive}:/")

data = {
    f"DiskSpace for drive:{drive}":[
        {"Total-GB": total // (2 ** 30)},
        {"Used-GB": used // (2 ** 30)},
        {"Free-GB":free // (2 ** 30)}
    ]}
json_data = json.dumps(data,indent=1)

with open("DiskSpace.json", "w") as outfile:
    outfile.write(json_data)
print(f'{GREEN}Done. It is located in the file called: DiskSpace.json{RESET}')