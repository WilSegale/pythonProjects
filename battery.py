# python script showing battery details
from colorama import *
import psutil

RED = Fore.RED

battery = psutil.sensors_battery()
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
if battery:
   battery = psutil.sensors_battery()
   print("Battery percentage:", battery.percent)
   print("Power plugged in:", battery.power_plugged)
   print("Battery left:", convertTime(battery.secsleft))

else:
    print(f"{RED}No battery found.")