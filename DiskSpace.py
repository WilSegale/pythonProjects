from colorama import *
import shutil
import os

total,used,free = shutil.disk_usage("/")
os.system('cls'if os.name=='nt' else "clear")
print("DiskSpace")
print(Fore.YELLOW + "Total: %d GB" % (total // (2**30)))
print(Fore.RED + "Used: %d GB" % (used // (2**30)))
print(Fore.GREEN + "Free: %d GB" % (free // (2**30))+Fore.RESET)