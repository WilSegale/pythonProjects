import matplotlib.pyplot as plt

# Disk space data
disk_space = {
    'C:': 50,
    'D:': 20,
    'E:': 30,
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

