from DontEdit import *
from sys import platform
import shutil
import os

if platform == "darwin":
    #mac os
    MAIN = "Main DRIVE-"
    os.system("clear")

    def is_drive_connected(drive_letter):
        return os.path.exists(drive_letter + "/")

    print(MAIN)
    total,used,free = shutil.disk_usage("/")
    print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
    print(RED + "Used: %d GB " % (used // (2 ** 30)))
    print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
#linux
if platform == "linux":
    #linux os
    MAIN = "/"

    def is_drive_connected(drive_letter):
        return os.path.exists(drive_letter + "/")

    print(MAIN)
    total,used,free = shutil.disk_usage("/")
    print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
    print(RED + "Used: %d GB " % (used // (2 ** 30)))
    print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)

# Windows...
elif platform == "win32":
    DRIVE = "A"
    ExternialDrive= f"{DRIVE}: DRVIE-"
    MAINDrive = "C: DRIVE-"

    os.system('cls' if os.name=='nt' else "clear")

    def is_drive_connected(drive_letter):
        return os.path.exists(drive_letter + ":")


    def drive():

        if is_drive_connected(DRIVE) == True:
            #? THIS IS THE EXTERNIAL DRIVE OF THE COMPUTER
            total,used,free = shutil.disk_usage(f"{DRIVE}:/")
            print("DiskSpace")
            print(f"\n{ExternialDrive}")
            print(GREEN + "Total: %d TB " % (total // (1024 * 1024 * 1024 * 1024)))
            print(RED + "Used: %d GB " % (used // (2**30)))
            print(YELLOW + "Free: %d TB" % (free // (1024 * 1024 * 1024 * 1024))+Fore.RESET)
            
            # this is something that say that the top is the D drive and the bottom is the C drive
            print("-"*15)

            #! THIS IS THE MAIN DRIVE OF THE COMPUTER
            print(f"{MAINDrive}")
            total,used,free = shutil.disk_usage("C:/")
            print(GREEN +"Total: %d GB " % (total // (2 ** 30)))
            print(RED +"Used: %d GB " % (used // (2 ** 30)))
            print(YELLOW +"Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)

        else:
            #! THIS IS THE MAIN DRIVE OF THE COMPUTER
            print(f"{MAINDrive}")
            total,used,free = shutil.disk_usage("C:/")
            print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
            print(RED + "Used: %d GB " % (used // (2 ** 30)))
            print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
    drive()