import subprocess
import time

# Define the command to display the Zenity progress dialog
zenity_cmd = [
    "zenity",
    "--progress",
    "--title=Loading Bar",
    "--text=Loading...",
    "--auto-close",  # Automatically close when the progress reaches 100%
]

# Create a subprocess to run the Zenity command
process = subprocess.Popen(zenity_cmd, stdin=subprocess.PIPE, 
stdout=subprocess.PIPE, text=True)

# Function to update the progress bar
def update_progress(progress_value):
    process.stdin.write(f"{progress_value}\n")
    process.stdin.flush()

try:
    # Simulate a time-consuming task
    for i in range(1, 101):
        update_progress(i)  # Update the progress bar
        time.sleep(0.1)  # Simulate some work
except KeyboardInterrupt:
    # Handle if the user cancels the operation
    process.stdin.write("100\n")  # Set progress to 100% to close the dialog
    process.stdin.flush()
    process.terminate()  # Terminate the Zenity process

# Close the Zenity process
process.stdin.close()
process.stdout.close()
process.wait()


