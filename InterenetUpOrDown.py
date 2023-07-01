from colorama import *
import socket
import time

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
            print(f"{Style.BRIGHT}{Fore.GREEN}Internet is up and running! {Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Internet seems to be down.{Fore.RESET}")
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nYou have closed the program')
        break
