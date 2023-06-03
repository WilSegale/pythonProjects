import matplotlib.pyplot as plt
import shutil

total,used,free = shutil.disk_usage("/")

# Data for the bar chart
labels = ['Used', 'Free',"total"]
DiskData = [used, free, total]
colors = ['red', 'yellow', 'green']

# Plot the bar chart
plt.bar(labels, DiskData, color=colors)
plt.xlabel('Space')
plt.ylabel('Size (in GB)')
plt.title('Disk Space Usage')
plt.show()