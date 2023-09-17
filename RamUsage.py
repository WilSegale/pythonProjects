from DontEdit import *
import psutil

MACOS = 'darwin'
LINUX = 'linux'

if platform == MACOS or platform == LINUX:
    def get_ram_usage():
        virtual_memory = psutil.virtual_memory()
        used_ram = virtual_memory.used
        total_ram = virtual_memory.total
        return used_ram, total_ram

    def get_ram_usage_percentage():
        ram_percentage = psutil.virtual_memory().percent
        return ram_percentage

    if __name__ == "__main__":
        used_ram, total_ram = get_ram_usage()
        ram_percentage = get_ram_usage_percentage()

        
        if ram_percentage >= 50:
            print(f"{BRIGHT}{RED}Warning: RAM usage is high!{RESET}")
            print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
            print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
            print("Amount of RAM left to use: {:.2f} GB".format((total_ram - used_ram) / (1024 ** 3)))
            print(f"RAM Usage Percentage: {BRIGHT}{RED}{ram_percentage:.2f}%{RESET}")
        else:
            print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
            print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
            print("Amount of RAM left to use: {:.2f} GB".format((total_ram - used_ram) / (1024 ** 3)))
            print(f"RAM Usage Percentage: {GREEN}{ram_percentage:.2f}%{RESET}")
else:
    def get_ram_usage():
        virtual_memory = psutil.virtual_memory()
        used_ram = virtual_memory.used
        total_ram = virtual_memory.total
        return used_ram, total_ram

    def get_ram_usage_percentage():
        ram_percentage = psutil.virtual_memory().percent
        return ram_percentage

    if __name__ == "__main__":
        used_ram, total_ram = get_ram_usage()
        ram_percentage = get_ram_usage_percentage()

        
        if ram_percentage >= 50:
            print(f"Warning: RAM usage is high!")
            print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
            print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
            print("Amount of RAM left to use: {:.2f} GB".format((total_ram - used_ram) / (1024 ** 3)))
            print(f"RAM Usage Percentage: {ram_percentage:.2f}%")
        else:
            print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
            print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
            print("Amount of RAM left to use: {:.2f} GB".format((total_ram - used_ram) / (1024 ** 3)))
            print(f"RAM Usage Percentage: {ram_percentage:.2f}%")