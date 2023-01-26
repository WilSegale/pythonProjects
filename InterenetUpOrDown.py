from colorama import *
import requests

GREEN = Fore.GREEN;
RED = Fore.RED;
try:
    response = requests.get("https://www.google.com")
    response.raise_for_status()
    print(f"{GREEN}The internet is up!")
except requests.exceptions.RequestException as e:
    print(f"{RED}The internet is down!")

