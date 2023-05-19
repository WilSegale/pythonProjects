import json
import shutil
from colorama import *

GREEN = Fore.GREEN
RESET = Fore.RESET
total, used, free = shutil.disk_usage("/")

data = {
    "DiskSpace for MAIN DRIVE":[
        {"Total-GB": total // (2 ** 30)}, 
        {"Used-GB": used // (2 ** 30)},
        {"Free-GB":free // (2 ** 30)}
    ]}
json_data = json.dumps(data,indent=4)

with open("DiskSpace.json", "w") as outfile:
    outfile.write(json_data)
print(f'{GREEN}Done. It is located in the file called: DiskSpace.json{RESET}')
