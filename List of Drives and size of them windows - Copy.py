import psutil
import matplotlib.pyplot as plt

def get_drive_capacity(drive_path):
    drive = psutil.disk_usage(drive_path)
    total = drive.total
    free = drive.free
    used = drive.used
    print(f"Total: {total // (2 ** 30)} GB")
    print(f"Free: {free // (2 ** 30)} GB")
    print(f"Used: {used // (2 ** 30)} GB")
    return used, free, total

def main():
    drive_paths = [drive.device for drive in psutil.disk_partitions()]
    
    if not drive_paths:
        print("No drives found on the system.")
        return

    print("Available drives:")
    for i, drive_path in enumerate(drive_paths):
        print(f"{i + 1}. {drive_path}")
    
    while True:
        try:
            choice = int(input("Select a drive (1, 2, etc.) or enter 0 to quit: "))
            if choice == 0:
                break
            if 1 <= choice <= len(drive_paths):
                selected_drive = drive_paths[choice - 1]
                used_capacity, free_capacity, total_capacity = get_drive_capacity(selected_drive)
                print(f"Capacity information for {selected_drive}:")
                print(f"Used: {used_capacity // (2 ** 30)} GB")
                print(f"Free: {free_capacity // (2 ** 30)} GB")
                print(f"Total: {total_capacity // (2 ** 30)} GB")
            else:
                print("Invalid choice. Please select a valid drive or enter 0 to quit.")
        except ValueError:
            print("Invalid input. Please enter a number or enter 0 to quit.")

if __name__ == "__main__":
    main()
