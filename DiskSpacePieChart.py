from colorama import *
import shutil
import matplotlib.pyplot as plt
total,used,free = shutil.disk_usage("/")

# data for the pie chart
labels = ['Free',"used"]
sizes = [free, used]
print(Fore.GREEN + "Total: %d GB " % (total // (2 ** 30)))
print(Fore.RED + "Used: %d GB " % (used // (2 ** 30)))
print(Fore.YELLOW + "Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)
# create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Disk Space Usage")
plt.show()
