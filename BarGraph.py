from DontEdit import *

def loadingBar(iterations, delay=0.1, width=40):
    for load in range(iterations + 1):
        progress = load / iterations
        bar_length = int(progress * width)
        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)
        percentage = int(progress * 100)
        
        print(f'\rLoading [{bar}] {percentage}% ', end='', flush=False)
        time.sleep(delay)

loadingBar(50)

total,used,free = shutil.disk_usage("/")

total_gb = total // (2 ** 30)
used_gb = used // (2 ** 30)
free_gb = free // (2 ** 30)

# Data for the bar chart
labels = [f'Used {used_gb}GB', 
          f'Free {free_gb}GB',
          f'total {total_gb}GB']

DiskData = [used_gb, free_gb, total_gb]


print(f"\n{RED}Used: {used_gb}") 
print(f"{YELLOW}Free: {free_gb}") 
print(f"{GREEN}Total: {total_gb}\
        {RESET}")

# Plot the bar chart
plt.bar(labels, DiskData, color=colors)
plt.xlabel('Space')
plt.ylabel('Size (in GB)')
plt.title('Disk Space Usage')
plt.show()
