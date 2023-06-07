import matplotlib.pyplot as plt
from colorama import *
from numpy import *
import readline
import os

quit = ["exit", 
        "quit", 
        "EXIT()",
        "exit()",
        "EXIT",
        "Exit",
        "QUIT",
        "Quit",
        "QUIT()"]

GREEN = Fore.GREEN
RESET = Fore.RESET
try:
    def get_drive_capacity(drive_path):
        total = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
        free = os.statvfs(drive_path).f_bavail * os.statvfs(drive_path).f_frsize
        used = total - free
        print(f"Total: {total // (2 ** 30)}")
        print(f"Free: {free // (2 ** 30)}")
        print(f"Used: {used // (2 ** 30)}")
        return used, free, total

    directory = "/Volumes"

    os.system(f"ls -l {directory}")

    print(f"{GREEN}Enter the external hard drive ex(EXTERNAL_HARDWARE){RESET}")

    # Define autocomplete function for external hard drive input
    def autocomplete(text, state):
        options = [name for name in os.listdir(directory) if name.startswith(text)]
        if state < len(options):
            return options[state[1]]
        else:
            return None

    # Enable autocomplete for input_path
    readline.parse_and_bind('tab: complete')
    readline.set_completer(autocomplete)
    while True:
        input_path = input(">>> ")
        if input_path in quit:
            print("[-] Exiting...")
            break
        # if the user inputs only "/" it only shows the main drive
        if input_path == "/":
            drive_paths = ["/"]

            drive_names = []

            total_capacities = []
            free_capacities = []
            used_capacities = []

            # Iterate over drive paths
            for drive_path in drive_paths:
                used_capacity, free_capacity, total_capacity = get_drive_capacity(drive_path)
                drive_names.append(drive_path)
                used_capacities.append(used_capacity // (2 ** 30))
                free_capacities.append(free_capacity  // (2 ** 30))
                total_capacities.append(total_capacity  // (2 ** 30)) 


            fig, ax = plt.subplots()
            bar_width = 100

            # Calculate the positions of the bars
            index = arange(len(drive_names))

            # Plot the bars
            ax.bar(index, used_capacities, bar_width, label='Used')
            ax.bar(index + bar_width, free_capacities, bar_width, label='Free')
            ax.bar(index + 2 * bar_width, total_capacities, bar_width, label='Total')

            ax.set_xlabel('Drive')
            ax.set_ylabel('Capacity')
            ax.set_title(f'Capacity of Drives for {drive_paths}')
            ax.set_xticks(index + bar_width)
            ax.set_xticklabels(drive_names, rotation=45)
            ax.legend()

            plt.show()
            
        elif input_path == "":
            print('ERROR: INPUT PATH MUST BE SPECIFIED.')

        # List of drive paths
        else:
            drive_paths = [f"/Volumes/{input_path}"]

            drive_names = []

            total_capacities = []
            free_capacities = []
            used_capacities = []

            # Iterate over drive paths
            for drive_path in drive_paths:
                used_capacity, free_capacity, total_capacity = get_drive_capacity(drive_path)
                drive_names.append(drive_path)
                used_capacities.append(used_capacity // (2 ** 30))
                free_capacities.append(free_capacity  // (2 ** 30))
                total_capacities.append(total_capacity  // (2 ** 30)) 


            fig, ax = plt.subplots()
            bar_width = 100

            # Calculate the positions of the bars
            index = arange(len(drive_names))

            # Plot the bars
            ax.bar(index, used_capacities, bar_width, label='Used')
            ax.bar(index + bar_width, free_capacities, bar_width, label='Free')
            ax.bar(index + 2 * bar_width, total_capacities, bar_width, label='Total')

            ax.set_xlabel('Drive')
            ax.set_ylabel('Capacity')
            ax.set_title(f'Capacity of Drives for {drive_paths}')
            ax.set_xticks(index + bar_width)
            ax.set_xticklabels(drive_names, rotation=45)
            ax.legend()

            plt.show()
except KeyboardInterrupt:
    print("\n[-] Exting program")
