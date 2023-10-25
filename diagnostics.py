from DontEdit import *
import subprocess

diagnostic = open("diagnostics.txt", "w")

try:
    # Define a function to run shell commands and capture their output
    def run_command(command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"

    # List of diagnostic commands
    diagnostic_commands = [
        "ping google.com -t 3",
        "traceroute google.com",
        "csrutil status",
        "sudo pfctl -s info",
        "system_profiler SPSoftwareDataType",
        "networksetup -listallnetworkservices",
        "networksetup -listallhardwareports",
        "df -h",
        "mount",
        "ps aux",
        "ps -ef | grep -v grep | awk '{print $2}'",
        "dscl . -list /Users",
        "cat /var/log/system.log",
        "nslookup google.com",
        "sudo pfctl -sa",
        "vm_stat"
    ]

    # Execute each diagnostic command and print the output
    for command in diagnostic_commands:
        
        
        html_output = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>diagnostics</title>
                </head>
                <body>
                    <h1>Diagnostics Commands</h1>
                    <p>COMMAND: {command}</p>
                    <p>OUTPUT: {run_command(command)}</p>
                </body>
                </html>
                """
        
        with open("diagnostics.html", "a") as html_file:
            html_file.write(html_output)
        
        print(f"Running command: {command}\n")
        result = run_command(command)
        print(result)
        print("=" * 40)

        print(f"Running command: {command}\n", file=diagnostic)
        print(result, file=diagnostic)
        print("=" * 40, file=diagnostic)  # Separation line

    # You can add more commands or remove any you don't need.
    print(f"{BRIGHT}{GREEN}\nFinished running all commands.{RESET}")

except KeyboardInterrupt:
    print("\nInterrupted by user.")
