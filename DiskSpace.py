from colorama import *
import shutil
import os

D = "D: DRVIE-"
C = "C: DRIVE-"

os.system('cls' if os.name=='nt' else "clear")

def is_drive_connected(drive_letter):
    return os.path.exists(drive_letter + ":")
    
if is_drive_connected("D") == True:
    
    #? THIS IS THE EXTERNIAL DRIVE OF THE COMPUTER
    total,used,free = shutil.disk_usage("D:/")
    print("DiskSpace")
    print(f"\n{D}")
    print(Fore.GREEN + "Total: %d TB " % (total // (1024 * 1024 * 1024 * 1024)))
    print(Fore.RED + "Used: %d GB " % (used // (2**30)))
    print(Fore.YELLOW + "Free: %d TB" % (free // (1024 * 1024 * 1024 * 1024))+Fore.RESET)
    
    #! THIS IS THE MAIN DRIVE OF THE COMPUTER
    print(f"\n{C}")
    total,used,free = shutil.disk_usage("C:/")
    print(Fore.GREEN +"Total: %d GB " % (total // (2 ** 30)))
    print(Fore.RED +"Used: %d GB " % (used // (2 ** 30)))
    print(Fore.YELLOW +"Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
else:
    #! THIS IS THE MAIN DRIVE OF THE COMPUTER

    print(f"{C}")
    total,used,free = shutil.disk_usage("C:/")
    print(Fore.GREEN + "Total: %d GB " % (total // (2 ** 30)))
    print(Fore.RED + "Used: %d GB " % (used // (2 ** 30)))
    print(Fore.YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)