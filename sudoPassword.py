from colorama import *
import getpass

GREEN = Fore.GREEN;
RED = Fore.RED;
BRIGHT = Style.BRIGHT;
RESET = Fore.RESET
def authenticate():
    sudo_password = getpass.getpass("Enter your sudo password: ")
    
    # Check if the entered password is correct
    if sudo_password == "Password":
        print(f"{BRIGHT}{GREEN}Authentication successful!{RESET}") 
        #Perform actions requiring sudo privileges here
    else:
        print(f"{BRIGHT}{RED}Authentication failed!")

authenticate()
