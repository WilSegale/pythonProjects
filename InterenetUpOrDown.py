from colorama import *
import requests
GREEN = Fore.GREEN;
RED = Fore.RED;
response = requests.get("https://www.google.com")
response.raise_for_status()
try:
    print(f"{GREEN}The internet is up!")
except:
    print(f"{RED}Internet is down")