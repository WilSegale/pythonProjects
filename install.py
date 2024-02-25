import subprocess
import matplotlib
matplotlib.use('Agg')

install = input("Would you like to install the requirements for this folder (y/n): ")
def install_requirements():

    if install.lower() == 'y':
        subprocess.run(["pip3", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully")

    elif install.lower() == 'n':
        print("Requirements installation skipped")
    else:
        print("Invalid input, requirements installation skipped")
install_requirements()