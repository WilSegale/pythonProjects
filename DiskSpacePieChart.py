from colorama import *
import shutil
import matplotlib.pyplot as plt

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