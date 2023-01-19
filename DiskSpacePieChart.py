from colorama import *
import shutil
import matplotlib.pyplot as plt
total,used,free = shutil.disk_usage("/")

# data for the pie chart
labels = ['', 'Free',"used"]
sizes = [total, free, used]

# create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Disk Space Usage")
plt.show()
