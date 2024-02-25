import subprocess  # Module for spawning new processes
import importlib.metadata  # Module for accessing metadata about Python packages

# Constants
Install = ["install", "i", "in"]  # List of commands to install packages
Uninstall = ["uninstall", "u", "un"]  # List of commands to uninstall packages
GREEN = "\033[32m"  # ANSI escape sequence for green color
RESET = "\033[0m"  # ANSI escape sequence to reset color
file_path = "requirements.txt"  # Path to the file containing package names

def is_package_installed(package_name):
    """
    Check if a package is installed.

    Args:
    - package_name (str): The name of the package to check.

    Returns:
    - bool: True if the package is installed, False otherwise.
    """
    try:
        importlib.metadata.version(package_name)  # Attempt to get package version
        return True  # Package is installed
    except importlib.metadata.PackageNotFoundError:
        return False  # Package is not installed

def install_requirements():
    """
    Install or uninstall requirements based on user input.
    """
    # Prompt user to choose between installing or uninstalling requirements
    action = input("Would you like to install or uninstall the requirements for this folder (Install/Uninstall): ").lower()

    # Install requirements
    if action in Install:
        with open(file_path, 'r') as file:
            packages = file.readlines()  # Read package names from requirements file
            packages = [package.strip() for package in packages]  # Remove leading/trailing whitespace and newline characters
            sorted_packages = sorted(packages, key=len)  # Sort by length of package names

            for package_name in sorted_packages:
                if not is_package_installed(package_name):  # Check if package is not installed
                    print(f"\nInstalling {package_name}...")  # Inform user about installation process
                    subprocess.run(["pip3", "install", package_name])  # Execute pip install command
                else:
                    print(f"{package_name} is {GREEN}installed{RESET}")  # Inform user that package is already installed

    # Uninstall requirements
    elif action in Uninstall:
         with open(file_path, 'r') as file:
            packages = [package.strip() for package in packages]  # Remove leading/trailing whitespace and newline characters
            packages = file.readlines()  # Read package names from requirements file
            sorted_packages = sorted(packages, key=len)  # Sort by length of package names

            for package_name in sorted_packages:
                if not is_package_installed(package_name):  # Check if package is not installed
                    subprocess.run(["pip3", "uninstall", package_name, "-y"])  # Execute pip uninstall command
                    print(f"\nInstalling {package_name}...")  # Inform user about installation process
                else:
                    print(f"{package_name} is {GREEN}uninstalled{RESET}")  # Inform user that package is already uninstalled
    
    # Handle invalid input
    else:
        print(f"\n[-] Invalid input, requirements installation skipped")  # Inform user about invalid input

# Call the function to install or uninstall requirements based on user input
install_requirements()