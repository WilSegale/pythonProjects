import subprocess
import psutil

def is_disk_encrypted(disk_path):
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.device == disk_path:
            if partition.fstype != '':
                # If the partition has a file system, it is likely not encrypted
                return False
            else:
                # If the partition doesn't have a file system, check if it's encrypted
                cmd = ['dmsetup', 'table', '--target', 'crypt', '--showkeys', '--nosync', partition.device]
                try:
                    output = subprocess.check_output(cmd)
                    if output:
                        # If there is output, it means the disk is encrypted
                        return True
                except subprocess.CalledProcessError:
                    # If an error occurs, assume the disk is not encrypted
                    return False

    # Disk not found
    return False

# Example usage
disk_path = input(">>> ")  # Replace with the path to your disk or partition
encrypted = is_disk_encrypted(disk_path)
if encrypted:
    print(f'''The disk "{disk_path}" is encrypted.''')
else:
    print(f'''The disk "{disk_path}" is not encrypted.''') 