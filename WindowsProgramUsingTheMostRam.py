import psutil
import os

while True:
    def find_process_with_most_memory():
        max_memory = 0
        max_memory_process = None

        for process in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                process_info = process.info
                pid = process_info['pid']
                name = process_info['name']

                memory_info = process_info['memory_info']

                if memory_info is not None:
                    # Get the Resident Set Size (RSS) in bytes
                    memory_usage = memory_info.rss

                    if memory_usage > max_memory:
                        max_memory = memory_usage
                        max_memory_process = (pid, name, memory_usage)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return max_memory_process

    if __name__ == "__main__":
        max_memory_process = find_process_with_most_memory()

        if max_memory_process:
            pid, name, memory_usage = max_memory_process
            print(f"Process with the most memory usage:\n"
                  f"PID: {pid}\n"
                  f"Name: {name}\n"
                  f"Memory Usage: {memory_usage / (1024 * 1024):.2f} MB")

            try:
                process = psutil.Process(pid)
                process.terminate()
            except psutil.NoSuchProcess:
                print("Process already exited.")
        else:
            print("No processes found.")
