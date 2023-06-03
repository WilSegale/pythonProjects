from colorama import *
import os
import matplotlib.pyplot as plt

GREEN = Fore.GREEN
RESET = Fore.RESET

def get_drive_capacity(drive_path):
   total_bytes = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
   free_bytes = os.statvfs(drive_path).f_bavail * os.statvfs(drive_path).f_frsize
   used_bytes = total_bytes - free_bytes
    
   return used_bytes

directory = "/Volumes"

os.system(f"ls -l {directory}")

print(f"{GREEN}Enter the external hard drive ex(EXTERNAL_HARDWARE){RESET}")
input_path = input(">>> ")

# List of drive paths
drive_paths = ["/", f"/Volumes/{input_path}"]  # input the list of the drive path

drive_names = []
used_capacities = []

# Iterate over drive paths
for drive_path in drive_paths:
   drive_capacity = get_drive_capacity(drive_path)
   drive_names.append(drive_path)
   used_capacities.append(drive_capacity)

# Plotting the bar graph
fig, ax = plt.subplots()
ax.bar(drive_names, used_capacities)

ax.set_xlabel('Drive')
ax.set_ylabel('Used Capacity')
ax.set_title('Used Capacity of Drives')

plt.xticks(rotation=45)

plt.show()
