import psutil

# get disk usage statistics
disk = psutil.disk_usage("/")
total = disk.total / (1024.0 ** 3)
used = disk.used / (1024.0 ** 3)
free = disk.free / (1024.0 ** 3)

# calculate and display amount of free space
print("Total disk space: {:.2f} GB".format(total))
print("Used disk space: {:.2f} GB".format(used))
print("Free disk space: {:.2f} GB".format(free))
