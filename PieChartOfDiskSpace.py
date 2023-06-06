import shutil
import matplotlib.pyplot as plt
total,used,free = shutil.disk_usage("/")

# Disk space data
disk_space = {
    total // (2 ** 30):total,
    used // (2 ** 30):used,
    free // (2 ** 30):free
}

# Pie chart
labels = list(disk_space.keys())
sizes = list(disk_space.values())

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Aspect ratio
plt.axis('equal')

# Title
plt.title('Disk Space')

# Display the chart
plt.show()


