import subprocess

def get_desktop_hard_drive_name():
    try:
        # Run the diskutil command to get information about disks and volumes
        result = subprocess.run(['diskutil', 'info', '/'], capture_output=True, text=True, check=True)
        # Split the output by lines
        lines = result.stdout.split('\n')
        # Loop through each line to find the volume name
        for line in lines:
            if 'Volume Name:' in line:
                # Extract the volume name
                volume_name = line.split(':')[1].strip()
                return volume_name
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    desktop_hard_drive_name = get_desktop_hard_drive_name()
    if desktop_hard_drive_name:
        print("Desktop Hard Drive Name:", desktop_hard_drive_name)
    else:
        print("Failed to retrieve desktop hard drive name.")
