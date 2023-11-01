
from DontEdit import *  # Assuming DontEdit contains the BRIGHT and color constants
import subprocess
import platform
import os


try:
    def is_disk_encrypted(disk_path):
        try:
            output = subprocess.check_output(["diskutil", "info", "-plist", disk_path])
            output = output.decode("utf-8")
            
            # Look for the string indicating encryption
            if "FileVault" in output:
                return True
            else:
                return False
        except subprocess.CalledProcessError:
            return False

    def Windows():
        if platform.system() == 'Windows':
            print(f"{RED}{BRIGHT}[-]{RESET} Wrong OS. This program only works on (Linux and Mac OS X).")
        else:
            if os.geteuid() == 0:
                print(f"{BRIGHT}{ORANGE_Start}WARNING:{ORANGE_END} It's recommended not to run this program with sudo.")
                print(f"Running the program with sudo privileges might have unintended consequences.")
                print(f"Consider running the program without sudo.")
                exit(1)
            else:
                # Example usage
                disk_path = input("Enter the disk identifier (e.g., /): ")
                encrypted = is_disk_encrypted(disk_path)

                if encrypted:
                    print(f"The disk '{disk_path}' is encrypted.")
                else:
                    print(f"The disk '{disk_path}' is not encrypted.")
    
    Windows()  # Call the Windows function to execute the code
    
except KeyboardInterrupt:
    print("\n[-] Exiting program")
