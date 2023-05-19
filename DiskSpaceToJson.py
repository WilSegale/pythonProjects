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

    print(f"drive: {get_drives()}")   # On my PC, this prints ['A', 'C', 'D', 'F', 'H']

    drive = input(f"Drive: ")
    total, used, free = shutil.disk_usage(f"{drive}:/")
    JSON_OUTPUT = {
        f"DiskSpace for drive:{drive.upper()}":[
            {"Total-GB": total // (2 ** 30)},
            {"Used-GB": used // (2 ** 30)},
            {"Free-GB":free // (2 ** 30)}
        ]
    }
    
    json_data = json.dumps(JSON_OUTPUT,indent=4)

    with open("DiskSpace.json", "w") as outfile:
        outfile.write(json_data)
    print(f'{GREEN}Done. It is located in the file called: DiskSpace.json{RESET}')