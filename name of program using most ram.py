import psutil
RamProgram = open("RAM PROGRAM.txt", "w")
def get_processes_by_memory():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            process_info = process.info
            if process_info['memory_info'] is not None:
                processes.append((process_info['pid'], process_info['name'], process_info['memory_info'].rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return sorted(processes, key=lambda x: x[2], reverse=True)

def main():
    print("Top processes by memory usage:")
    print("{:<10} {:<30} {:<15}".format("PID", "Name", "Memory Usage"))
    print("-" * 60)

    processes = get_processes_by_memory()

    for pid, name, memory in processes[:10]:  # Display top 10 processes
        print("{:<10} {:<30} {:<15}".format(pid, name, f"{memory / (1024 * 1024):.2f} MB"))
        print("{:<10} {:<30} {:<15}".format(pid, name, f"{memory / (1024 * 1024):.2f} MB"),file=RamProgram)


if __name__ == "__main__":
    main()
