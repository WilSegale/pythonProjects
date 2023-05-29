from colorama import *
import os

GREEN = Fore.GREEN
RESET = Fore.RESET

def get_drive_capacity(drive_path):
   total_bytes = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
   free_bytes = os.statvfs(drive_path).f_bavail * os.statvfs(drive_path).f_frsize
   used_bytes = total_bytes - free_bytes
    
   if total_bytes < 1024**2:
      return f"Total: {total_bytes} bytes, Free: {free_bytes} bytes, Used: {used_bytes} bytes"
   
   elif total_bytes < 1024**3:
      return f"Total: {total_bytes / 1024**2} MB, \nFree: {free_bytes / 1024**2} MB, \nUsed: {used_bytes / 1024**2} MB"
   
   elif total_bytes < 1024**4:
      return f"Total: {total_bytes / 1024**3} GB, \nFree: {free_bytes / 1024**3} GB, \nUsed: {used_bytes / 1024**3} GB"
   
   else:
      return f"Total: {total_bytes / 1024**4} TB, \nFree: {free_bytes / 1024**4} TB, \nUsed: {used_bytes / 1024**4} TB"

directory = "/Volumes"

os.system(f"ls -l {directory}")

print(f"{GREEN}Enter the external hard drive ex(EXTERNAL_HARDWARE){RESET}")
input_path = input(">>> ")

# List of drive paths
drive_paths = ["/", f"/Volumes/{input_path}"]  # input the list of the drive path

# Iterate over drive paths
for drive_path in drive_paths:
   drive_capacity = get_drive_capacity(drive_path)
   print(f"Drive: {drive_path}\n{drive_capacity}\n")
