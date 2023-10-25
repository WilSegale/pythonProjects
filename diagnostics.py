import subprocess

diagnostic = open("diagnostics.txt", "a")

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
        "sudo pfctl -s info"
    ]

    # Execute each diagnostic command and print the output
    for command in diagnostic_commands:
        print(f"Running command: {command}\n")
        print(f"Running command: {command}\n", file=diagnostic)
        result = run_command(command)
        print(result)
        print(result, file=diagnostic)
        print("=" * 40)
        print("=" * 40, file=diagnostic)  # Separation line

    # You can add more commands or remove any you don't need.

except KeyboardInterrupt:
    print("\nInterrupted by user.")
