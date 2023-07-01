import psutil

def get_mac_hard_drives():
    hard_drives = []
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.device.startswith('/dev/disk'):
            hard_drives.append(partition.device)
    return hard_drives

# Usage
mac_hard_drives = get_mac_hard_drives()
for drive in mac_hard_drives:
    print(drive)
