import subprocess
import matplotlib
from DontEdit import *
matplotlib.use('Agg')

install = input("Would you like to install or uninstall the requirements for this folder (Install/Uninstall): ")

def install_requirements():

    if install.lower() in Install:
        subprocess.run(["pip3", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully")

    elif install.lower() in Uninstall:
        subprocess.run(["pip3", "uninstall", "requirements.txt" , "-y"])
        print(f"{GREEN}[+]{RESET} Requirements uninstallation successfully")

    else:
        print("Invalid input, requirements installation skipped")

install_requirements()