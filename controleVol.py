import subprocess

def set_volume(level):
    command = f"osascript -e 'set volume output volume {level}'"
    subprocess.call(command, shell=True)

def increase_volume():
    subprocess.call("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'", shell=True)

def decrease_volume():
    subprocess.call("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'", shell=True)

# Example usage
print("Input the number you want how loud your computer is.")
set_volume(input(">>> "))  # Set volume to 50%
increase_volume()  # Increase volume by 10%
decrease_volume()  # Decrease volume by 10%

