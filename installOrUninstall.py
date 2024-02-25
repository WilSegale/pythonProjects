import subprocess  # Import subprocess module for running shell commands
import matplotlib  # Import matplotlib for plotting functionalities
from DontEdit import *  # Import custom module DontEdit, assuming it contains predefined lists Install and Uninstall
matplotlib.use('Agg')  # Set matplotlib backend to 'Agg' for non-interactive plotting

# Prompt user to choose between installing or uninstalling requirements
install = input("Would you like to install or uninstall the requirements for this folder (Install/Uninstall): ")

def install_requirements():
    # Check if user wants to install requirements
    if install.lower() in Install:  # Check if user input matches any element in Install list
        subprocess.run(["pip3", "install", "-r", "requirements.txt"])  # Run pip to install requirements from requirements.txt
        print(f"{GREEN}[+]{RESET} Requirements installed successfully")

    # Check if user wants to uninstall requirements
    elif install.lower() in Uninstall:  # Check if user input matches any element in Uninstall list
        subprocess.run(["pip3", "uninstall", "requirements.txt" , "-y"])  # Run pip to uninstall requirements listed in requirements.txt
        print(f"{GREEN}[+]{RESET} Requirements uninstallation successfully")

    # Handle invalid input
    else:
        print(f"{RED}[-]{RESET} Invalid input, requirements installation skipped")

# Call the function to install or uninstall requirements based on user input
install_requirements()
