from DontEdit import *
import os
import shutil
from sys import platform

def is_drive_connected(drive_letter):
    return os.path.exists(drive_letter + "/")

def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free

def main():
    if platform == "darwin":
        # macOS
        MAIN_DRIVE = "Main DRIVE-"
        os.system("clear")
        root_path = "/"
        
    elif platform == "linux":
        # Linux
        MAIN_DRIVE = "/"
        os.system("clear")
        root_path = "/"
        
    elif platform == "win32":
        # Windows
        EXTERNAL_DRIVE = "A"
        MAIN_DRIVE = "C: DRIVE-"
        os.system('cls' if os.name == 'nt' else "clear")
        root_path = f"{EXTERNAL_DRIVE}:/"
        
    else:
        print("Unsupported platform")
        return
    
    if is_drive_connected(root_path):
        print("DiskSpace")
        
        if platform == "win32":
            print(f"\n{EXTERNAL_DRIVE}")
            total, used, free = get_disk_usage(root_path)
            print(GREEN + "Total: %d TB " % (total // (1024 * 1024 * 1024 * 1024)))
            print(RED + "Used: %d GB " % (used // (2 ** 30)))
            print(YELLOW + "Free: %d TB" % (free // (1024 * 1024 * 1024 * 1024)) + RESET)
            print("-" * 15)
            
        print(f"{MAIN_DRIVE}")
        total, used, free = get_disk_usage(root_path)
        print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
        print(RED + "Used: %d GB " % (used // (2 ** 30)))
        print(YELLOW + "Free: %d GB " % (free // (2 ** 30)) + RESET)
    else:
        print(f"{MAIN_DRIVE}")
        total, used, free = get_disk_usage(root_path)
        print(GREEN + "Total: %d GB " % (total // (2 ** 30)))
        print(RED + "Used: %d GB " % (used // (2 ** 30)))
        print(YELLOW + "Free: %d GB " % (free // (2 ** 30)) + RESET)

if __name__ == "__main__":
    main()
