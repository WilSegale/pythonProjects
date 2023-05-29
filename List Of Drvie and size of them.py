import os

def get_drive_capacity(drive_path):
   total_bytes = os.statvfs(drive_path).f_blocks * os.statvfs(drive_path).f_frsize
   if total_bytes < 1024**2:
      return f"{total_bytes} bytes"
   elif total_bytes < 1024**3:
      return f"{total_bytes / 1024**2} MB"
   elif total_bytes < 1024**4:
      return f"{total_bytes / 1024**3} GB"
   else:
      return f"{total_bytes / 1024**4} TB"

# List of drive paths
drive_paths = ["/"]# input the list of the drive path

# Iterate over drive paths
for drive_path in drive_paths:
   drive_capacity = get_drive_capacity(drive_path)
   if drive_capacity == "":
      print ("Drive capacity")
   else:
      print(f"Drive: {drive_path}\nCapacity: {drive_capacity}\n")
