import os

def list_drive_contents(drive_path):
    try:
        contents = os.listdir(drive_path)
        return contents
    except OSError as e:
        print(f"Error: {e}")
        return []

def main():
    drives = ["C:\\", "D:\\", "E:\\"]  # Add the drive letters you want to check
    print("Available drives:")
    for drive in drives:
        if os.path.exists(drive):
            print(drive)
    
    drive_name = input("Enter the drive letter (e.g., C:): ")
    drive_path = drive_name + "\\"
    
    if not os.path.exists(drive_path):
        print("Drive not found.")
        return
    
    contents = list_drive_contents(drive_path)
    print(f"Contents of drive {drive_name}:")
    print("+"*25)
    
    for item in contents:
        print(f"{item}")

if __name__ == "__main__":
    main()
