from DontEdit import *
from commands import *

diagnostic = open("diagnostics.html", "w")

try:
    # Define a function to run shell commands and capture their output
    def run_command(command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"

    # Define a function to generate a formatted HTML block for a command and its output
    def generate_command_html(command, output):
        return f"""
        <div class="command-block">
            <h2>Command:</h2>
            <pre id="command" class="command">[{command}]</pre>
            <h2>Output:</h2>
            <pre id="output" class="output">{output}</pre>
        </div>
        """

    # Open the HTML file and write the advanced structure
    html_output = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Diagnostics</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                .command {
                    font-weight: bold;
                    color: green;
                    font-size: 24px;                
                }
                .output {
                    white-space: pre-line;
                }
                .command-block {
                    border: 1px solid #ccc;
                    padding: 10px;
                    margin: 10px;
                }
                h1 {
                    font-size: 24px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <h1>Diagnostics Commands</h1>
        """

    # You can append more command and output sections as needed, and then close the HTML document.
    # For example:

    # Finally, close the HTML document
    html_output += """
        </body>
        </html>
    """

# Write the HTML content to a file or use it as needed.


    diagnostic.write(html_output)

    # List of diagnostic commands for Windows and Mac
    diagnostic_commands = Windows_diagnostic_commands if platform.system() == "Windows" else MacOs_diagnostic_commands

    # Execute each diagnostic command and append the HTML output
    for command in diagnostic_commands:
        result = run_command(command)
        command_html = generate_command_html(command, result)
        diagnostic.write(command_html)

        print(f"Running command: {command}\n")
        print(result)
        print("=" * 40)

    # Close the HTML file
    diagnostic.write("</body></html>")
    diagnostic.close()

    # You can add more commands or remove any you don't need.
    print(f"{BRIGHT}{GREEN}\n[+]{RESET} Finished running all commands.")

except KeyboardInterrupt:
    print("\nInterrupted by the user.")
