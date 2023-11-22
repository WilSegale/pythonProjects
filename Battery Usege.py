import psutil

def get_power_usage():
    # Get CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")

if __name__ == "__main__":
    get_power_usage()
