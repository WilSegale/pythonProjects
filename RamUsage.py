import psutil

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

    print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
    print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
    print(f"RAM Usage Percentage: {ram_percentage:.2f}%")
