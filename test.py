import time
import psutil

boot_time = psutil.boot_time()
current_time = time.time()
uptime = int(current_time - boot_time)
print("Uptime: ", uptime)