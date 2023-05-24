# python script showing battery details
from colorama import *
import psutil

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

battery = psutil.sensors_battery()

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

if battery:
    battery = psutil.sensors_battery()
    if battery.percent >= int(50):
        print(f"{BRIGHT}{YELLOW}Battery percentage: {GREEN}{battery.percent}%{RESET}")
        print(f"{BRIGHT}{YELLOW}Power plugged in: {RED}{battery.power_plugged}{RESET}")
        print(f"{BRIGHT}{YELLOW}Battery left: {GREEN}{convertTime(battery.secsleft)}{RESET}")
    else:
        print(f"{BRIGHT}{YELLOW}Battery percentage: {RED}{battery.percent}%{RESET}")
        print(f"{YELLOW}Power plugged in: {GREEN}{battery.power_plugged}{RESET}")
        print(f"{YELLOW}Battery left: {RED}{convertTime(battery.secsleft)}{RESET}")
else:
    print(f"{RED}{BRIGHT}[-] No battery found.{RESET}")