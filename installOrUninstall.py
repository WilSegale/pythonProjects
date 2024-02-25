import subprocess
import importlib.metadata

# Constants
Install = ["install", "i", "in"]
Uninstall = ["uninstall", "u", "un"]
GREEN = "\033[32m"
RESET = "\033[0m"
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
        importlib.metadata.version(package_name)
        return True
    except importlib.metadata.PackageNotFoundError:
        return False

def install_requirements():
    """
    Install or uninstall requirements based on user input.
    """
    # Prompt user to choose between installing or uninstalling requirements
    action = input("Would you like to install or uninstall the requirements for this folder (Install/Uninstall): ").lower()

    # Install requirements
    if action in Install:
        with open(file_path, 'r') as file:
            packages = file.readlines()
            packages = [package.strip() for package in packages]  # Remove leading/trailing whitespace and newline characters
            sorted_packages = sorted(packages, key=len)  # Sort by length of package names

            for package_name in sorted_packages:
                if not is_package_installed(package_name):
                    print(f"\nInstalling {package_name}...")
                    subprocess.run(["pip3", "install", package_name])
                else:
                    print(f"{package_name} is already {GREEN}installed{RESET}")

    # Uninstall requirements
    elif action in Uninstall:
         with open(file_path, 'r') as file:
            packages = file.readlines()
            packages = [package.strip() for package in packages]  # Remove leading/trailing whitespace and newline characters
            sorted_packages = sorted(packages, key=len)  # Sort by length of package names

            for package_name in sorted_packages:
                if not is_package_installed(package_name):
                    print(f"\nInstalling {package_name}...")
                    subprocess.run(["pip3", "uninstall", package_name, "-y"])
                else:
                    print(f"{package_name} is already {GREEN}uninstalled{RESET}")
    # Handle invalid input
    else:
        print(f"\n[-] Invalid input, requirements installation skipped")

# Call the function to install or uninstall requirements based on user input
install_requirements()
