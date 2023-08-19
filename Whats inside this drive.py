import os

def list_drive_contents(drive_path):
    try:
        contents = os.listdir(drive_path)
        return contents
    except OSError as e:
        print(f"Error: {e}")
        return []

def main():
    drives = os.listdir("/Volumes")
    print("Available drives:")
    for drive in drives:
        print(drive)
    
    drive_name = input("Enter the name of the drive: ")
    external_drive_path = os.path.join("/Volumes", drive_name)
    
    if not os.path.exists(external_drive_path):
        print("Drive not found.")
        return
    
    contents = list_drive_contents(external_drive_path)
    print("Contents of the drive:")
    for item in contents:
        print(item)

if __name__ == "__main__":
    main()
