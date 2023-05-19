import os
from sys import platform

def start():
   if platform == "win32":
      os.system("dir");
      CHOICE = input("Enter your choice: ");
      os.system(f"python3 {CHOICE}");
   else:
      os.system("ls -l {CHOICE}");
      CHOICE = input("Enter your choice: ");
      os.system(f"python3 {CHOICE}");
start()