import os
import psutil

# Get the current process ID
pid = os.getpid()

# Monitor CPU and memory usage
cpu_percent = psutil.cpu_percent(interval=1)
memory_usage = psutil.Process(pid).memory_info().rss

print(f"CPU Percent: {cpu_percent}%")
print(f"Memory Usage: {memory_usage} bytes")
