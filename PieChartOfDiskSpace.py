import matplotlib.pyplot as plt
from colorama import *
import shutil

CYAN = Fore.CYAN
Gray = Fore.LIGHTBLACK_EX
RESET = Fore.RESET


total,used,free = shutil.disk_usage("/")

# Disk space data
disk_space = {
    total // (2 ** 30):total,
    used // (2 ** 30):used
}

# Pie chart
labels = list(disk_space.keys())
sizes = list(disk_space.values())
explode = (0.1, 10, 0)  # Explode the first slice

# Custom colors
colors = ['CYAN', 'lightgray']

# Create a pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.01f%%', startangle=59, shadow=True)

# Aspect ratio
plt.axis('on')

# Title
plt.title('Disk Space')

# Legend
plt.legend(labels, loc='best')
print(f"FREE: {CYAN}{total // (2 ** 30)}{RESET}")
print(f"USED: {Gray}{used // (2 ** 30)}{RESET}")

# Display the chart
plt.show()

