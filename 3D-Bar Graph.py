# Bar graph data
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from colorama import *
from sys import platform
import shutil
import string

#the array that contains the name of colors so the graph has some color to it
colors = ['green', 
          'red', 
          'yellow']

# the array that contains the name of exiting words
exit = ["exit", 
        "quit", 
        "exit()",
        "EXIT()",
        "QUIT()",
        ""]
#the variables that contains the name of the colors and the RESET color
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def get_drives():
    #sees if the user is on a Windows machine
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
            print(f"drive: {get_drives()}")   # On my PC, this prints ['A', 'C', 'D', 'F', 'H']

        while True:
            print("Input the name of the drive you want to the amount of space remaning on")
            drives = input(">>> ")

            if drives in exit:
                print("Exiting...")
                break

            total,used,free = shutil.disk_usage(drives+":/")
            total // (2 ** 30)
            free // (2 ** 30)
            used // (2 ** 30) 
            labels = ['total',
                    'Used', 
                    'Free']
            
            values = [total,
                    used,
                    free]
                    
            # shows the data for the total data that you have on your disk
            print(GREEN + "Total: %d GB " % (total // (2 ** 30)))

            # shows the data for the used amount of data that you have on your disk
            print(RED + "Used: %d GB " % (used // (2 ** 30)))
            
            # shows the data for the free amount of data that you have on your disk
            print(YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
            
            plt.show()
            fig, ax = plt.subplots()

            # Create bar graph
            ax.bar(labels, values, color=colors)

            # Add shadow effect to bars
            for patch in ax.patches:
                patch.set_alpha(0.5)
    else:
        #if the user is not on a Windows machine it says "Not supported on this platform"
        print(f"{RED}Not supported on this platform{RESET}")

get_drives()