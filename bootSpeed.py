from DontEdit import *

def loadingBar(iterations, delay=0.1, width=40):
    for load in range(iterations + 1):
        progress = load / iterations
        bar_length = int(progress * width)
        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)
        percentage = int(progress * 100)
        
        print(f'\rLOADING [{bar}] {percentage}% ', end='', flush=True)
        time.sleep(delay)

loadingBar(50)
start_time = time.time()

# Your program code goes here

end_time = time.time()
boot_speed = end_time - start_time

print(f"\nBoot speed: {boot_speed :,.2} seconds")

