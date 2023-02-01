from sys import platform
from colorama import *
import shutil
import os

if platform == "darwin":
    #mac os
    MAIN = "Main DRIVE-"

    os.system('cls' if os.name=='nt' else "clear")

    def is_drive_connected(drive_letter):
        return os.path.exists(drive_letter + "/")

    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW

    total,used,free = shutil.disk_usage("/")
    print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
    print(RED + "Used: %d GB " % (used // (2 ** 30)))
    print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)

# Windows...
elif platform == "win32":
    D = "D: DRVIE-"
    C = "C: DRIVE-"

    os.system('cls' if os.name=='nt' else "clear")

    def is_drive_connected(drive_letter):
        return os.path.exists(drive_letter + ":")

    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW

    def drive():

        if is_drive_connected("D") == True:
            #? THIS IS THE EXTERNIAL DRIVE OF THE COMPUTER
            total,used,free = shutil.disk_usage("D:/")
            print("DiskSpace")
            print(f"\n{D}")
            print(GREEN + "Total: %d TB " % (total // (1024 * 1024 * 1024 * 1024)))
            print(RED + "Used: %d GB " % (used // (2**30)))
            print(YELLOW + "Free: %d TB" % (free // (1024 * 1024 * 1024 * 1024))+Fore.RESET)
            
            # this is something that say that the top is the D drive and the bottom is the C drive
            print("-"*15)

            #! THIS IS THE MAIN DRIVE OF THE COMPUTER
            print(f"{C}")
            total,used,free = shutil.disk_usage("C:/")
            print(GREEN +"Total: %d GB " % (total // (2 ** 30)))
            print(RED +"Used: %d GB " % (used // (2 ** 30)))
            print(YELLOW +"Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)

        else:
            #! THIS IS THE MAIN DRIVE OF THE COMPUTER
            print(f"{C}")
            total,used,free = shutil.disk_usage("C:/")
            print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
            print(RED + "Used: %d GB " % (used // (2 ** 30)))
            print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
    drive()