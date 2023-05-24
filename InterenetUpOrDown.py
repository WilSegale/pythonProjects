from colorama import *
import socket
import time

GREEN = Fore.GREEN;
RED = Fore.RED;
RESET = Style.RESET_ALL;

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
while True:
    try: 
        if is_connected():
            print(f"{GREEN}Internet is up and running!{RESET}")
            break
        else:
            print(f"{RED}Internet seems to be down.{RESET}")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f'\n{RED}[-| You have closed the program')
        break
