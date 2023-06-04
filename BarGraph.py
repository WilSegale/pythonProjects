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

# Plot the bar chart
plt.bar(labels, DiskData, color=colors)
plt.xlabel('Space')
plt.ylabel('Size (in GB)')
plt.title('Disk Space Usage')
plt.show()