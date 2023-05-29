from colorama import *
import os

GREEN = Fore.GREEN
RESET = Fore.RESET

def get_drive_capacity(drive_path):
   total_bytes = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
   if total_bytes < 1024**2:
      return f"{total_bytes} bytes"
   
   elif total_bytes < 1024**3:
      return f"{total_bytes / 1024**2} MB"
   
   elif total_bytes < 1024**4:
      return f"{total_bytes / 1024**3} GB"
   
   else:
      return f"{total_bytes / 1024**4} TB"

directory = "/Volumes"

os.system(f"ls -l {directory}")

print(f"{GREEN}Enter the externial hard drive ex(EXTERNAL_HARDWARE){RESET}")
input_path = input(">>> ")

# List of drive paths
drive_paths = ["/",f"/Volumes/{input_path}"]# input the list of the drive path

# Iterate over drive paths
for drive_path in drive_paths:
   drive_capacity = get_drive_capacity(drive_path)
   
   print(f"Drive: {drive_path}\nCapacity: {drive_capacity}\n")
