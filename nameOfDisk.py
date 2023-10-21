import psutil

def get_disk_name():
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        if partition.mountpoint == '/':
            return partition.device

disk_name = get_disk_name()
print(f"Disk Name: {disk_name}")