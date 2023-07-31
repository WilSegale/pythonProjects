from DontEdit import *
import matplotlib.pyplot as plt
import shutil

total,used,free = shutil.disk_usage("/")

total_gb = total // (2 ** 30)
used_gb = used // (2 ** 30)
free_gb = free // (2 ** 30)

# Data for the bar chart
labels = ['Used', 'Free',"total"]
DiskData = [used_gb, free_gb, total_gb]
colors = ['red', 'yellow', 'green']
print(f"{RED}Used: {used_gb}") 
print(f"{YELLOW}Free: {free_gb}") 
print(f"{GREEN}Total: {total_gb}{RESET}")

# Plot the bar chart
plt.bar(labels, DiskData, color=colors)
plt.xlabel('Space')
plt.ylabel('Size (in GB)')
plt.title('Disk Space Usage')
plt.show()
