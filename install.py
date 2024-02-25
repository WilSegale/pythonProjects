import subprocess
from DontEdit import *

install = input("Would you like to install the requirements for this folder (y/n): ")

if install.lower() == 'y':
    subprocess.run(["pip3", "install", "-r", "requirements.txt"])
    print("Requirements installed successfully")
