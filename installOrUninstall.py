import subprocess  # Import subprocess module for running shell commands
import importlib.metadata
Install = ["install", "INSTALL", "Install", "i", "I","in","IN"]
Uninstall = ["uninstall", "UNINSTALL", "Uninstall", "u", "U","un","UN"]
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
    install = input("Would you like to install or uninstall the requirements for this folder (Install/Uninstall): ")

    # Check if user wants to install requirements
    if install.lower() in Install:  # Check if user input matches any element in Install list
        with open(file_path, 'r') as file:
            for line in file:
                package_name = line.strip()  # Remove leading/trailing whitespace and newline characters
                if not is_package_installed(package_name):
                    print(f"\nInstalling {package_name}...")
                    subprocess.run(["pip3", "install", "-r", file_path])
                else:
                    print(f"{package_name} is already {GREEN}installed{RESET}")
    # Check if user wants to uninstall requirements
    elif install.lower() in Uninstall:  # Check if user input matches any element in Uninstall list
        subprocess.run(["pip3", "uninstall", "-r", "requirements.txt", "-y"])
        with open(file_path, 'r') as file:
            for line in file:
                package_name = line.strip()  # Remove leading/trailing whitespace and newline characters
                if not is_package_installed(package_name):
                    print(f"\nUninstalling {package_name}...")
                    subprocess.run(["pip3", "uninstall", file_path, "-y"])
                else:
                    print(f"{package_name} is already {GREEN}uninstalled{RESET}")
        print(f"\n[+] Requirements uninstalled")
    # Handle invalid input
    else:
        print(f"\n[-] Invalid input, requirements installation skipped")

# Call the function to install or uninstall requirements based on user input
install_requirements()
