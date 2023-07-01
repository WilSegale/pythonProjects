import psutil

def check_disk_changes():
    previous_disks = set(psutil.disk_partitions())
    
    while True:
        current_disks = set(psutil.disk_partitions())
        
        new_disks = current_disks - previous_disks
        removed_disks = previous_disks - current_disks
        
        if new_disks:
            print("New disk(s) installed:")
            for disk in new_disks:
                print(f"- {disk.device}")
        
        if removed_disks:
            print("Disk(s) removed:")
            for disk in removed_disks:
                print(f"- {disk.device}")
        
        previous_disks = current_disks

# Call the function to start monitoring disk changes
check_disk_changes()

