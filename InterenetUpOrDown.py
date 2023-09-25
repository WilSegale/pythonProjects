from DontEdit import *


init()  # Initialize colorama

def loadingBar(iterations, delay=0.1, width=40):
    for load in range(iterations + 1):
        progress = load / iterations
        bar_length = int(progress * width)
        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)
        percentage = int(progress * 100)
        
        print(f'\r[{bar}] {percentage}% ', end='', flush=True)
        time.sleep(delay)

loadingBar(50)


def is_connected():
    try:
        # Connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

while True:
    try:
        if is_connected():
            print(f"\n{Style.BRIGHT}{GREEN}Internet is up and running! {RESET}")
            break
        else:
            print(f"{RED}Internet seems to be down.{RESET}")
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nYou have closed the program')
        break
