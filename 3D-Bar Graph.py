import matplotlib.pyplot as plt
from colorama import *
from sys import platform
import shutil
import string
# The array that contains the name of colors so the graph has some color to it
colors = ['green', 'red', 'yellow']
exit = ["exit", "quit", "exit", "quit"]

RED = Fore.RED;
GREEN = Fore.GREEN;
YELLOW = Fore.YELLOW;
RESET = Style.RESET_ALL;

def get_drives():
    if platform == "win32":
        from ctypes import windll
        def get_drives():
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(letter)
                bitmask >>= 1

            return drives

        if __name__ == '__main__':
            # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
            print(f"drive: {get_drives()}")

        while True:
            print("Input the name of the drive you want to the amount of space remaining on")
            drives = input(">>> ")

            if drives in exit:
                print("Exiting...")
                break

            total, used, free = shutil.disk_usage(drives+":/")
            total_gb = total // (2 ** 30)
            used_gb = used // (2 ** 30)
            free_gb = free // (2 ** 30)

            labels = ['Total', 'Used', 'Free']
            values = [total_gb, used_gb, free_gb]

            # shows the data for the total data that you have on your disk
            print("Total: %d GB" % total_gb)

            # shows the data for the used amount of data that you have on your disk
            print("Used: %d GB" % used_gb)

            # shows the data for the free amount of data that you have on your disk
            print("Free: %d GB" % free_gb)

            fig, ax = plt.subplots()

            # Create bar graph
            ax.bar(labels, values, color=colors)

            # Add shadow effect to bars
            for patch in ax.patches:
                patch.set_alpha(0.5)

            # Add numbers on top of each bar with respective colors
            for i, value in enumerate(values):
                color = colors[i]
                ax.text(i, value + 1, str(value), ha='right', fontsize=10)

            plt.show()
    else:
        # if the user is not on a Windows machine it says "Not supported on this platform"
        print(f"{RED}[-] Not supported on this platform{GREEN}")

get_drives()