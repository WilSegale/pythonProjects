from colorama import *
import shutil
import matplotlib.pyplot as plt

#_____________________________Terminal of disk space____________________________________#
D = "D: DRVIE-"
C = "C: DRIVE-"
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW

print(f"\n{D}")
total,used,free = shutil.disk_usage("D:/")
print(GREEN + "Total: %d TB " % (total // (1024 * 1024 * 1024 * 1024)))
print(RED + "Used: %d GB " % (used // (2**30)))
print(YELLOW + "Free: %d TB" % (free // (1024 * 1024 * 1024 * 1024))+Fore.RESET)

# this is something that say that the top is the D drive and the bottom is the C drive
print("-"*15)

print(f"{C}")
#! THIS IS THE MAIN DRIVE OF THE COMPUTER
total,used,free = shutil.disk_usage("C:/")
print(GREEN +"Total: %d GB " % (total // (2 ** 30)))
print(RED +"Used: %d GB " % (used // (2 ** 30)))
print(YELLOW +"Free: %d GB " % (free // (2 ** 30))+ Fore.RESET)

#_____________________________Pie chart of disk space____________________________________#

#! D Drive Usage
total,used,free = shutil.disk_usage("D:/")

# data for the pie chart
labels = ['', 'Free',"used"]
sizes = [total, free, used]

# create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Disk Space Usage For D drive.")
plt.show()

#! C Drive Usage
total,used,free = shutil.disk_usage("C:/")

# data for the pie chart
labels = ['Free',"used"]
sizes = [free, used]

# create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Disk Space Usage For C drive.")
plt.show()