import psutil

def get_total_ram():
    virtual_memory = psutil.virtual_memory()
    total_ram_gb = virtual_memory.total / (1024.0 ** 3)
    return total_ram_gb

if __name__ == "__main__":
    total_ram = get_total_ram()
    print(f"Total RAM: {total_ram:.2f} GB")


