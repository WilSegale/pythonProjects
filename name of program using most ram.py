# Import the psutil library to retrieve information about system processes
import psutil

# Open a text file to write the information about programs using the most RAM
RamProgram = open("RAM PROGRAM.txt", "w")

# Function to get processes sorted by memory usage
def get_processes_by_memory():
    processes = []
    # Iterate over all running processes
    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Get process information
            process_info = process.info
            # Check if memory_info is not None to avoid AttributeError
            if process_info['memory_info'] is not None:
                # Append process details to the list
                processes.append((process_info['pid'], process_info['name'], process_info['memory_info'].rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions that may occur while accessing process information
            pass
    # Return the list of processes sorted by memory usage in descending order
    return sorted(processes, key=lambda x: x[2], reverse=True)

# Main function to display and write the top processes by memory usage
def main():
    print("Top processes by memory usage:")
    print("{:<10} {:<30} {:<15}".format("PID", "Name", "Memory Usage"))
    print("-" * 60)
    print("{:<10} {:<30} {:<15}".format("PID", "Name", "Memory Usage"),file=RamProgram)
    print("-" * 60, file=RamProgram)

    # Get processes by memory usage
    processes = get_processes_by_memory()

    # Display and write the details of the top 10 processes
    for pid, name, memory in processes[:10]:
        print("{:<10} {:<30} {:<15}".format(pid, name, f"{memory / (1024 * 1024):.2f} MB"))
        print("-" * 60)
        # Write the details to the text file
        print("{:<10} {:<30} {:<15}".format(pid, name, f"{memory / (1024 * 1024):.2f} MB"), file=RamProgram)
        print("-" * 60,file=RamProgram)
# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

# Close the text file after writing
RamProgram.close()
