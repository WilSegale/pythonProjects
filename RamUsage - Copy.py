import psutil 
import sys
from DontEdit import *

MACOS = "darwin"

# Define a function to retrieve RAM usage information
def get_ram_usage():
    virtual_memory = psutil.virtual_memory()
    used_ram = virtual_memory.used
    total_ram = virtual_memory.total
    return used_ram, total_ram

# Define a function to retrieve RAM usage percentage
def get_ram_usage_percentage():
    ram_percentage = psutil.virtual_memory().percent
    return ram_percentage

# Define a function to print RAM-related information
def print_ram_info(used_ram, total_ram, ram_percentage):
    print(f"\nUsed RAM: {used_ram / (1024 ** 3):.2f} GB")
    print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
    print("Amount of RAM left to use: {:.2f} GB".format((total_ram - used_ram) / (1024 ** 3)))
    print(f"RAM Usage Percentage: {ram_percentage:.2f}%")
    print()

# Entry point of the program
if __name__ == "__main__":
    # Get RAM usage information
    used_ram, total_ram = get_ram_usage()
    ram_percentage = get_ram_usage_percentage()

    platform = sys.platform

    # Check the platform (OS) to determine the warning message color
    if platform == MACOS:  # Note the change from 'in' to '=='
        if ram_percentage >= 50:
            # Print a warning message if RAM usage is high
            print(f"{BRIGHT}{RED}[!] Warning: RAM usage is high [!]{RESET}")
        else:
            # Print a normal message if RAM usage is normal
            print(f"{GREEN}RAM usage is normal.{RESET}")

    # Print RAM-related information
    print_ram_info(used_ram, total_ram, ram_percentage)
