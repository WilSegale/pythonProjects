from DontEdit import *

def get_boot_time():
    boot_time = psutil.boot_time()
    boot_time_datetime = datetime.datetime.fromtimestamp(boot_time)
    return boot_time_datetime

# Usage
boot_time = get_boot_time()
formatted_boot_time = boot_time.strftime("%Y-%m-%d %I:%M:%S %p")
print("System Boot Time:", formatted_boot_time)
