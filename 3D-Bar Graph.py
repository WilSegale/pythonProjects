
from DontEdit import *

# The array that contains the name of colors so the graph has some color to it
colors = ['green', 'red', 'yellow']
try:
    def get_drives():
        if platform.system() == "Windows":
            from ctypes import windll
            
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(letter)
                bitmask >>= 1

            return drives
        else:
            return None  # Return None for non-Windows platforms

    if __name__ == '__main__':
        # Check if the platform is not "win32" (Windows)
        if platform.system() != "Windows":
            print(f"{BRIGHT}{RED}[-]{RESET} Not supported for your OS")
        else:
            # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
            print(f"Drive: {get_drives()}")

            print("Input the name of the drive you want to see the amount of space remaining on")
            drives = input(">>> ")

            total, used, free = shutil.disk_usage(drives + ":/")
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

            # Create a bar graph
            ax.bar(labels, values, color=colors)

            # Add a shadow effect to bars
            for patch in ax.patches:
                patch.set_alpha(0.5)

            # Add numbers on top of each bar with respective colors
            for i, value in enumerate(values):
                color = colors[i]
                ax.text(i, value + 1, str(value), ha='center', fontsize=10)

            # Put a label on the y-axis
            ax.set_ylabel("Amount (GB)")  # Add y-axis label

            plt.show()
except KeyboardInterrupt:
    print("\nExiting...")
