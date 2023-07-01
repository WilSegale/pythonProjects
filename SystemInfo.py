import psutil
import subprocess

# Get the system's CPU usage
cpu_percent = psutil.cpu_percent()
print("CPU usage: ", cpu_percent)

# Get the system's memory usage
memory = psutil.virtual_memory()
print("Total memory: ", memory.total / (1024 ** 2), "MB")
print("Used memory: ", memory.used / (1024 ** 2), "MB")
print("Free memory: ", memory.free / (1024 ** 2), "MB")

# Get the system's boot time
boot_time = psutil.boot_time()
print("Boot time: ", boot_time)

# Get the system's uptime
uptime = subprocess.check_output(['uptime']).decode()
print("Uptime: ", uptime)

# Get the system's users
users = psutil.users()
print("Users: ", users)
