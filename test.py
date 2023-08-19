import psutil
import matplotlib.pyplot as plt

def get_drive_info():
    drives = psutil.disk_partitions()
    drive_info = []
    
    for drive in drives:
        drive_info.append({
            'drive': drive.device,
            'mountpoint': drive.mountpoint,
            'fstype': drive.fstype
        })
    
    return drive_info

def create_bar_graph(drive_info):
    drives = [drive['drive'] for drive in drive_info]
    mountpoints = [drive['mountpoint'] for drive in drive_info]
    
    plt.bar(drives, mountpoints)
    plt.xlabel('Drives')
    plt.ylabel('Mount Points')
    plt.title('List of Drives and Mount Points')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    drive_info = get_drive_info()
    create_bar_graph(drive_info)

