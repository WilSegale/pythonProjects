import subprocess
import os
# Replace 'program_to_run.py' with the name of the Python program you want to run
os.system('ls')

ProgramToRun = input("Enter the name of the Python program you want to run: ")

program_name = ProgramToRun

# Run the program and capture its output and errors
try:
    output = subprocess.check_output(['python3', program_name], stderr=subprocess.STDOUT, universal_newlines=True)
    print("Program output:")
    print(output)
except subprocess.CalledProcessError as e:
    print("An error occurred:")
    print(e.output)

