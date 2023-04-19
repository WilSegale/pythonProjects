import psutil

partitions = psutil.disk_partitions()
disk_name = None
for partition in partitions:
    if partition.device == '/':
        disk_name = partition.mountpoint
        break

if disk_name is not None:
    print("Disk name:", disk_name)
else:
    print("Unable to determine disk name.")
