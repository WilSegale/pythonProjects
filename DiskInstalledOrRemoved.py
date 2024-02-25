import psutil
try:
    def check_disk_changes():
        previous_disks = set(psutil.disk_partitions())
        
        while True:
            current_disks = set(psutil.disk_partitions())
            
            new_disks = current_disks - previous_disks
            removed_disks = previous_disks - current_disks
            
            if previous_disks:
                for disk in previous_disks:
                    print(f"{disk.device}")
                    exit(1)
            if new_disks:
                partitions = psutil.disk_partitions(all=True)
                hard_drive_names = []
                for partition in partitions:
                    if partition.device and 'loop' not in partition.device:
                        hard_drive_names.append(partition.device)
                return hard_drive_names
            
            if removed_disks:
                print("Disk(s) removed:")
                for disk in removed_disks:
                    print(f"- {disk.device}")
            
            previous_disks = current_disks

    # Call the function to start monitoring disk changes
    check_disk_changes()
    
except KeyboardInterrupt:
    print("[-] Exiting...")