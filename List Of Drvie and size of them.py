from colorama import *
import os
import matplotlib.pyplot as plt
import readline

GREEN = Fore.GREEN
RESET = Fore.RESET

def get_drive_capacity(drive_path):
    total = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
    free = os.statvfs(drive_path).f_bavail * os.statvfs(drive_path).f_frsize
    used = total - free

    print(used // (2 ** 30))
    return used

directory = "/Volumes"

os.system(f"ls -l {directory}")

print(f"{GREEN}Enter the external hard drive ex(EXTERNAL_HARDWARE){RESET}")

# Define autocomplete function for external hard drive input
def autocomplete(text, state):
    options = [name for name in os.listdir(directory) if name.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Enable autocomplete for input_path
readline.parse_and_bind('tab: complete')
readline.set_completer(autocomplete)

input_path = input(">>> ")
if input_path == "/":
    drive_paths = ["/"]
    
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

# List of drive paths
else:
    drive_paths = ["/", f"/Volumes/{input_path}"]
    
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

