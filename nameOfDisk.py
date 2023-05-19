from colorama import *
import psutil

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

partitions = psutil.disk_partitions()
disk_name = None
for partition in partitions:
    if partition.device == '/':
        disk_name = partition.mountpoint
        break

if disk_name is not None:
    print(f"{GREEN}Disk name: {disk_name}{RESET}")
else:
    print(f"{RED}Unable to determine disk name.{RESET}")
